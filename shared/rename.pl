#! /usr/bin/perl -w
use strict;
use File::Find ();
use File::Basename;
use File::Spec;
use File::Copy;
use File::Path;
use autodie;
use Getopt::Long;
use Cwd;
# Set the variable $File::Find::dont_use_nlink if you're using AFS,
# since AFS cheats.

# for the convenience of &wanted calls, including -eval statements:
use vars qw/*name *dir *prune/;
*name   = *File::Find::name;
*dir    = *File::Find::dir;
*prune  = *File::Find::prune;

sub wanted_file;
sub wanted_dir;
sub remove_file;
sub remove_dir;
sub printd;
my $newfile;
my $dirname_old;
my $basename_old;
my $dirname_new;
my $basename_new;
my $cur_path_old;
my $cur_path_new;
my $cur_file_old;
my $cur_file_new;
my $abs_path_old;
my $abs_path_new;
my $abs_file_old;
my $abs_file_new;
my $prog_path;
my $prog_name;
my $gbase;
my $filename_old;
my ($usage, $help, $debug, $impl, $from_def);
my $found=0;
my $to_delete_dir=0;
my $to_delete_file=0;

#README
$usage =
"Replace abc terms with def terms in both text and filename.
On your root of local repo or path within local repo.
Before running this script, please make sure your repo is clean!
To clean your repo, following git commands can be used:

  git reset HEAD --hard; git clean -d -f

Also, remember to source shared/dotcshrc

  cd shared
  source dotcshrc

$prog_name --help  //Show this message
$prog_name         //without debug message but warning message
$prog_name --debug //with debug message and warning message
$prog_name --impl  //Operated under implementation related path anyway.
                       //Please apply this option on specific path you want to rename.
                       //ex. at implementation_tsmc_cln40lp/DEF_typical_cadence
                       //
$prog_name --from_def //under def database, catching ENV DEF_HOME instead of ABC_HOME

";


$help  = '';
$debug = '';
$impl  = '';

GetOptions (
  'help'       => \$help,
  'debug'      => \$debug,
  'impl'       => \$impl,
  'from_def' => \$from_def
);

# Traverse desired filesystems
if ($help) {
  print ("$usage\n");
} else {
  $prog_path = cwd();

  if ($from_def) {
    $gbase = dirname "$ENV{DEF_HOME}";
  } else {
    $gbase = dirname "$ENV{ABC_HOME}";
  }

  printd("program path : $prog_path\n");
  printd("def path   : $gbase\n");

  File::Find::find({wanted => \&wanted_file}, '.'); #replace text from Abc/abc/ABC to Def/def/DEF
                                                    #create file/path from Abc/abc/ABC to Def/def/DEF

  if ($to_delete_file) { #if matched abcs terms and a file/link to avoid failure of chdir of find method recursively
    #&printd ("unlink $abs_file_old in main wanted_file \n");
    #unlink "$abs_file_old";
    &printd ("git rm \'$abs_file_old\' in main wanted_file \n");

    system "git rm \'$abs_file_old\'";
  }

  File::Find::find({wanted => \&remove_dir}, '.');  #remove old dir with Abc/abc/ABC

  if ($to_delete_dir) { #if matched abcs terms and a directory to avoid failure of chdir of find method recursively
    #&printd ("$abs_file_old is a directory4 in main, rmtree it! \n");
    #&printd ("rmtree $abs_file_old, 1, 1 in main \n");

    #rmtree("$abs_file_old", 1, 1);
    &printd ("git rm -r \'$abs_file_old\' in main remove_dir \n");
    system "git rm -r \'$abs_file_old\'";
    #&printd ("git rm \'$abs_file_old\' in main remove_dir \n");
    #system "git rm \'$abs_file_old\'";
  }
}
exit;

sub printd {
  if ($debug) {
    print "$_[0]";
  }
}

#cp $newfile to dir($newfile)
sub wanted_file {

    if ($to_delete_file) { #if matched abcs terms and a file/link to avoid failure of chdir of find method recursively
      #&printd ("unlink $abs_file_old in wanted_file \n");
      #unlink "$abs_file_old";
      &printd ("git rm \'$abs_file_old\' in front of wanted_file \n");
      system "git rm \'$abs_file_old\'";
    }

   $to_delete_file = 0;

    print("name = $name in wanted_file\n"); #name is relative path

    $filename_old = basename $name;
    $abs_path_old = cwd();
    $abs_file_old = File::Spec->catfile($abs_path_old, $filename_old);
    $basename_old = File::Spec->abs2rel($abs_file_old, $gbase);
    $dirname_old  = File::Spec->abs2rel($abs_path_old, $gbase);

    &printd("abs_path_old = $abs_path_old \n");
    &printd("abs_file_old = $abs_file_old \n");

    &printd("dirname_old  = $dirname_old \n");
    &printd("basename_old = $basename_old \n");

    if ($dirname_old =~ /^.*\.git.*\z/s) {
      &printd ("bypass .git path : $dirname_old \n");
      return;
    }

    if ($impl) {
      if ($basename_old =~ /^.*(($prog_name)).*\z/s) {
        &printd ("bypass $prog_name file: $basename_old \n");
        return;
     } elsif ($basename_old =~ /^.*(txt|README).*\z/s) { #txt/README is the exception
        &printd ("txt/README is the exception not to bypass file: $basename_old \n");
      } elsif ($basename_old =~ /^.*(pdf|docs).*\z/s) {
        &printd ("bypass pdf/docs file: $basename_old \n");
        return;
      }
    } else {
      if ($basename_old =~ /^.*(implementation|($prog_name)).*\z/s) {
        &printd ("bypass implementation/$prog_name file: $basename_old \n");
        return;
      } elsif ($basename_old =~ /^.*(txt|README).*\z/s) { #txt/README is the exception
        &printd ("txt/README is the exception not to bypass file: $basename_old \n");
      } elsif ($basename_old =~ /^.*(pdf|docs).*\z/s) {
        &printd ("bypass pdf/docs file: $basename_old \n");
        return;
      }
    }

    #if ($abs_file_old =~ /^.*csv.*\z/s) {
    #  &printd ("bypass csv file: $abs_file_old\n");
    #  return;
    #}
    $found = 0;
    $found = ($basename_old =~ /^.*(abc|Abc|ABC).*\z/s);
    #}


    if (1) {
      #&printd("wanted_file found!\n");
      #&printd("abs_file_old = $abs_file_old\n");
      ($basename_new = $basename_old) =~ s/abc/def/g;
      $basename_new =~ s/Abc/Def/g;
      $basename_new =~ s/ABC/DEF/g;
      $abs_file_new = File::Spec->catfile($gbase, $basename_new);
      $abs_path_new = dirname $abs_file_new;

      &printd("abs_path_old = $abs_path_old \n");
      &printd("abs_file_old = $abs_file_old \n");
      &printd("abs_path_new = $abs_path_new \n");
      &printd("abs_file_new = $abs_file_new \n");

      #if (-e $abs_file_new) {
      #  &printd ("abs_file_new existed in wanted_file\n");
      #} else {
        if (-d $abs_file_old && $found) { #abs_file_new is a directory
          if (! -e $abs_file_new) {
            my ($dev, $ino, $mode, $nlink, $uid, $gid, $rdev,
            $size, $atime, $mtime, $ctime, $blksize, $blocks)
            = stat($abs_file_old);
            #&printd ("mkdir $abs_file_new $mode in wanted_file\n");
            #mkdir "$abs_file_new", $mode;
            &printd ("mkpath $abs_file_new, 1, $mode in wanted_file \n");
            mkpath("$abs_file_new", 1, $mode);
            &printd ("git add \'$abs_file_new\' in wanted_file \n");
            system "git add \'$abs_file_new\'";
          }
        } elsif (! -d $abs_file_old) {#abs_file_new is just a file
          if (-l $abs_file_old) { #abs_file_new is a link
            if ($found) {
              if (! -e $abs_path_new) { #if new fir not existed, mkdir it)
                my ($dev, $ino, $mode, $nlink, $uid, $gid, $rdev,
                $size, $atime, $mtime, $ctime, $blksize, $blocks)
                = stat($abs_path_old);
                #&printd( "mkdir $abs_path_new, $mode in wanted_file\n");
                #mkdir "$abs_path_new", $mode;
                &printd( "mkpath $abs_path_new, 1, $mode in wanted_file \n");
                mkpath("$abs_path_new", 1, $mode);
                &printd ("git add \'$abs_path_new\' in wanted_file \n");
                system "git add \'$abs_path_new\'";
              }
              if (! -e $abs_file_new) {
                &printd ("$abs_file_old is a link in wanted_file \n");
                my $link_target = readlink ($abs_file_old);
                $link_target =~ s/abc/def/g;
                $link_target =~ s/Abc/Def/g;
                $link_target =~ s/ABC/DEF/g;
                #system "link -s \'$link_target\' \'$abs_file_new\'";
                #$abs_file_new -> $link_target
                &printd ("symlink $link_target, $abs_file_new in wanted_file \n");
                symlink $link_target, $abs_file_new;
                #&printd ("link -s \'$link_target\' \'$abs_file_new\'\n");
                #&printd ("link -s \'$link_target\' \'$abs_file_new\'\n");
                &printd ("git add \'$abs_file_new\' in wanted_file \n");
                system "git add \'$abs_file_new\'";
                $to_delete_file = 1;
               #&printd ("unlink $abs_file_old in wanted_file \n");
                #unlink "$abs_file_old";
                #&printd ("git rm \'$abs_file_old\' in wanted_file \n");
                #system "git rm \'$abs_file_old\'";
              }
            }
          } else { #modify if it is just a file
            if (! -e $abs_path_new) { #if new fir not existed, mkdir it)
              my ($dev, $ino, $mode, $nlink, $uid, $gid, $rdev,
             $size, $atime, $mtime, $ctime, $blksize, $blocks)
              = stat($abs_path_old);
              #&printd( "mkdir $abs_path_new, $mode in wanted_file\n");
              #mkdir "$abs_path_new", $mode;
              &printd( "mkpath $abs_path_new, 1, $mode in wanted_file \n");
              mkpath("$abs_path_new", 1, $mode);
              &printd ("git add \'$abs_path_new\' in wanted_file \n");
              system "git add \'$abs_path_new\'";
            }
            if (-T $abs_file_old) { #modify only if it is a text file
              &printd ("modifying! $abs_file_old in wanted_file \n");
              #system "cp -f \'$abs_file_old\' \'$abs_file_old\'".'.replace';
              #&printd ("cp -f \'$abs_file_old\' \'$abs_file_old\'".'.replace'."\n");
              &printd ("copy $abs_file_old $abs_file_old".'.replace'." in wanted_file \n");
              copy ("$abs_file_old",  "$abs_file_old".'.replace');
              open my $fh_in,  '<', "$abs_file_old".'.replace';
              open my $fh_out, '>', "$abs_file_new";
              while (<$fh_in>) {
                s/abc/def/g;
                s/Abc/Def/g;
                s/ABC/DEF/g;
                print $fh_out $_;
              }
              #system "rm -f \'$abs_file_old\'".'.replace';
              &printd ("unlink $abs_file_old.replace in wanted_file \n");
              unlink "$abs_file_old".'.replace';
              close $fh_in;
              close $fh_out;
            } elsif ($found) { #binary and found
              &printd ("copying $abs_file_old is a binary file and found in wanted_file \n");
              copy ("$abs_file_old",  "$abs_file_new");
            }
            if ($found || -T $abs_file_old) {
              if ($abs_file_new =~ /^.*log.*\z/s) {
                &printd ("git add -f \'$abs_file_new\' in wanted_file \n");
                system "git add -f \'$abs_file_new\'";
              } else {
                &printd ("git add \'$abs_file_new\' in wanted_file \n");
                system "git add \'$abs_file_new\'";
              }
            }
            if ($found) {
              $to_delete_file = 1;
              #&printd ("unlink $abs_file_old in wanted_file \n");
              #unlink "$abs_file_old";
              #&printd ("git rm \'$abs_file_old\' in wanted_file \n");
              #system "git rm \'$abs_file_old\'";
            }
            #&printd  ("rm -f \'$abs_file_old\'".'.replace'." \n");
          }
        }
      }
}

sub remove_dir {

    if ($to_delete_dir) { #if matched abcs terms and a directory to avoid failure of chdir of find method recursively
      #&printd ("$abs_file_old is a directory4 in front of remove_dir, rmtree it! \n");
      #&printd ("rmtree $abs_file_old, 1, 1 in front of remove_dir \n");
      #rmtree("$abs_file_old", 1, 1);
      &printd ("git rm -r \'$abs_file_old\' in front of remove_dir \n");
      system "git rm -r \'$abs_file_old\'";

      #&printd ("git rm \'$abs_file_old\' in front of remove_dir \n");
      #system "git rm \'$abs_file_old\'";
    }

    $to_delete_dir = 0;

    print ("name = $name in remove_dir\n");

    $filename_old = basename $name;

    $abs_path_old = cwd();
    $abs_file_old = File::Spec->catfile($abs_path_old, $filename_old);
    $basename_old = File::Spec->abs2rel($abs_file_old, $gbase);
    $dirname_old  = File::Spec->abs2rel($abs_path_old, $gbase);

    &printd("abs_path_old = $abs_path_old \n");
    &printd("abs_file_old = $abs_file_old \n");
    &printd("dirname_old  = $dirname_old \n");
    &printd("basename_old = $basename_old \n");

    if ($dirname_old =~ /^.*\.git.*\z/s) {
      &printd ("bypass .git path : $dirname_old \n");
      return;
    }

    if ($impl) {
      if ($basename_old =~ /^.*(($prog_name)).*\z/s) {
        &printd ("bypass $prog_name file: $basename_old \n");
        return;
      } elsif ($basename_old =~ /^.*(txt|README).*\z/s) { #txt/README is the exception
        &printd ("txt/README is the exception not to bypass file: $basename_old \n");
      } elsif ($basename_old =~ /^.*(pdf|docs).*\z/s) {
        &printd ("bypass pdf/docs file: $basename_old \n");
        return;
      }
    } else {
      if ($basename_old =~ /^.*(implementation|($prog_name)).*\z/s) {
        &printd ("bypass implementation/$prog_name file: $basename_old \n");
        return;
      } elsif ($basename_old =~ /^.*(txt|README).*\z/s) { #txt/README is the exception
        &printd ("txt/README is the exception not to bypass file: $basename_old \n");
      } elsif ($basename_old =~ /^.*(pdf|docs).*\z/s) {
        &printd ("bypass pdf/docs file: $basename_old \n");
        return;
      }
    }

    #if ($abs_file_old =~ /^.*csv.*\z/s) {
    #  &printd ("bypass csv file: $abs_file_old \n");
    #  return;
    #}

    $found = 0;
    $found = ($basename_old =~ /^.*(abc|Abc|ABC).*\z/s);

    if ($found) {
      &printd ("remove_dir found! \n");
      #&printd("abs_file_old = $abs_file_old\n");
      ($basename_new = $basename_old) =~ s/abc/def/g;
      $basename_new =~ s/Abc/Def/g;
      $basename_new =~ s/ABC/DEF/g;
      $abs_file_new = File::Spec->catfile($gbase, $basename_new);
      $abs_path_new = dirname $abs_file_new;

      &printd ("abs_path_old = $abs_path_old \n");
      &printd ("abs_file_old = $abs_file_old \n");
      &printd ("abs_path_new = $abs_path_new \n");
      &printd ("abs_file_new = $abs_file_new \n");
      #Begin of main operation
      if (-d $abs_file_old) { #abs_file_old is a directory
        my ($dev, $ino, $mode, $nlink, $uid, $gid, $rdev,
        $size, $atime, $mtime, $ctime, $blksize, $blocks)
        = stat($abs_file_old);
        &printd ("nlink = $nlink, $abs_file_old \n");
        if ($nlink == 2) { #delete empty path only!
          $to_delete_dir = 1;
         #&printd ("$abs_file_old is a directory4 in rear of remove_dir, rmtree it! \n");
          #&printd ("rmtree $abs_file_old, 1, 1 in rear of remove_dir\n");
          #rmtree("$abs_file_old", 1, 1);
          #&printd ("git rm -r \'$abs_file_old\' in rear of remove_dir \n");
          #system "git rm -r \'$abs_file_old\'";
          #&printd ("git rm \'$abs_file_old\' in rear of remove_dir \n");
          #system "git rm \'$abs_file_old\'";
        }
      }
      #End of main operation
    }
}

