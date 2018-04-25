# POSIX comm implementation in Python 
Simple support an extra option -u, which causes comm to work when the input is not sorted.

## NAME
comm - select or reject lines common to two files

## SYNOPSIS
comm [-123u] file1 file2

## DESCRIPTION

The comm utility shall read file1 and file2, which should be ordered in the current collating sequence, and produce three text columns as output: lines only in file1, lines only in file2, and lines in both files.

If the lines in both files are not ordered according to the collating sequence of the current locale, the results are unspecified.

If the collating sequence of the current locale does not have a total ordering of all characters (see XBD LC_COLLATE) and any lines from the input files collate equally but are not identical, comm should treat them as different lines but may treat them as being the same. If it treats them as different, comm should expect them to be ordered according to a further byte-by-byte comparison using the collating sequence for the POSIX locale and if they are not ordered in this way, the output of comm can identify such lines as being both unique to file1 and unique to file2 instead of being in both files.

## OPTIONS

The comm utility shall conform to XBD Utility Syntax Guidelines .

The following options shall be supported:

-1
Suppress the output column of lines unique to file1.
-2
Suppress the output column of lines unique to file2.
-3
Suppress the output column of lines duplicated in file1 and file2.
-u
Causes comm to work when the input is not sorted.

## OPERANDS

The following operands shall be supported:

file1
A pathname of the first file to be compared. If file1 is '-', the standard input shall be used.
file2
A pathname of the second file to be compared. If file2 is '-', the standard input shall be used.
If both file1 and file2 refer to standard input or to the same FIFO special, block special, or character special file, the results are undefined.

### Reference:
http://pubs.opengroup.org/onlinepubs/9699919799/utilities/comm.html
