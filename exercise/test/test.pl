#!/usr/bin/perl
#print("hello world\n");

#my @tl = [a, b, c];
#my $a, $b, $c = @tl;
#print ("$a, $b, $c\n");

my $a, $b, $c;
($a, $b, @c) = ("apple", "banana", "cherry", "pipeapple");
print("$a\n");
print("$b\n");
print("@c\n");
