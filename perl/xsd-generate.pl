#!/usr/bin/perl
#
use XML::Pastor;

if($#ARGV < 0){
	exit;
}
my $file = shift;
my $prefix = shift . "::";

my $pastor = XML::Pastor->new();
$pastor->generate(  
	mode =>'offline',
	style => 'single',
	schema=>$file,
	class_prefix=>$prefix,
	destination=>'./',
);  
