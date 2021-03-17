#!/usr/bin/perl
#print("hello world\n");

#my @tl = [a, b, c];
#my $a, $b, $c = @tl;
#print ("$a, $b, $c\n");

#my $a, $b, $c;
#($a, $b, @c) = ("apple", "banana", "cherry", "pipeapple");
#print("$a\n");
#print("$b\n");
#print("@c\n");


#use Try::Tiny;

#my $total = 1;
#my $count = 0;
#my $result;
#eval {
#  ($result = $total /$count) or die "xxx";
#};
#
#  if ($@) {
#    print "An error occurred ($@), continuing\n";
#  }
#use autodie;
#my $filename = wilma;
#open my $fh, '<', $filename;
##open my $fh, '<', $filename;
##open my $fh, '<', $filename;
##open my $fh, '<', $filename;
#
#given ($@) {
#  #when ('open') {print "error from open"}
#}

#use 5.010;
#my $filename = wilma;
#open my $fh, '<', $filename;
#given ($@) {
#  when ('open') {print 'open'}
#}

#foreach my $person (qw/ fred wilma betty barney dino pebbles /) {
#  eval {
#    open my $fh, '<', $person or die "KKK '$person': $!";
#    my($total, $count);
#    while (<$fh>) {
#      $total += $_;
#      $count++;
#    }
#    #(my $ttt = $total/$count) or die "cant div by 0 : $!";
#      my $average = eval { $total/0 } // 'NaN'; # Inner eval
#      print "Average for file $person was $average\n";
#      #if ($@) {
#      #  print "An error occurred JJJ ($@), continuing\n";
#      #}
#    #&do_something($person, $average);
#  };
#  if ($@) {
#    print "An error occurred BBB ($@), continuing\n";
#  }
#}

use autodie;
foreach my $person (qw/ fred wilma betty barney dino pebbles /) {
    open my $fh, '<', $person or die "KKK '$person': $!";
}
