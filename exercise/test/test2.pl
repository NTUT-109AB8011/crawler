#! /usr/bin/perl -w
#if (@ARGV < 2) {
#  die ""
#}

my @a = qw /a1 a2 a3/;
my @b = qw /b1 b2 b3/;
my @c = qw /c1 c2 c3/;

print "\@a = @a\n", @a;
print ("\@b = @b\n"), @b;
print ("\@c = @c\n"), @c;

print ("\n");

@a = @b || @c;
print ("\@a = @a\n"), @a;
print ("\@b = @b\n"), @b;
print ("\@c = @c\n"), @c;

print ("\n");

@a = scalar(@b) || @c;
print ("\@a = @a\n"), @a;
print ("\@b = @b\n"), @b;
print ("\@c = @c\n"), @c;

print ("\n");

@a = @b ? @b : @c;
print ("\@a = @a\n"), @a;
print ("\@b = @b\n"), @b;
print ("\@c = @c\n"), @c;

