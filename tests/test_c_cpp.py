from strip_comments import strip

source = '''CHAPTER 4 : Commenting
PART 2 : COMMENTING AND NAMING

CHAPTER 4 : Commenting
4.1 Commenting fundamentals
4.2 Comment types
4.3 Header comments
4.4 File Header comment
4.5 Function header comments
4.6 Block comments
4.7 Trailing comments
4.8 Commenting data
4.9 The preprocessor and comments
4.10 Summary

<--Prev page | Next page -->

4.6 Block comments
Block comments are typically found within functions, between 'chunks' of code. They also appear in other parts of code, for example at the start of chunks of data. There are a number of common approaches to block comments, several of which are discussed below.

4.6.1 Comment size
There are about three different classifications of block comment, depending on its size:

A single line comment will commonly describe a simple item.
A multiple line comment, up to about 5 lines will summarize a more complex item or set of items.
A longer comment will describe even more, although this is now tending towards a major header comment.
Generally, it must be remembered that a block comment has a cost in vertical space and should give value for money. For example, it may be overkill for a block comment to be bigger than the chunk of function code that it describes.

4.6.2 Positioning the comment
A block comment usually describes code below it. This association can be made clearer by using some method to explicitly associate it more closely with the code that it describes.

Using blank lines
A simple principle is to use a blank line above the comment to physically place it closer to the line below than the line above:



    ResetParms();

/* Close all remaining open windows */
    for ( Win = 0; Win < NofWins; Win++ )
        CloseWin( Win );



This, however, causes a possible problem where the comment and the code are not immediately distiguishable. A solution, at the cost of more vertical space, is to put a blank line below the comment:



    ResetParms();

/* Close all remaining open windows */

    for ( Win = 0; Win < NofWins; Win++ )
        CloseWin( Win );



Indenting the comment
A common method of positioning is to vertically align the comment with the current indent level. This helps to associate the comment with the code below, and preserves the line of indentation. However, this reduces the amount of horizontal space available for comment, particularly at deeper levels of nesting, and may make it more difficult to distinguish between comments and code:



    ResetParms();

    /* Close all remaining open windows */
    for ( Win = 0; Win < NofWins; Win++ )
        CloseWin( Win );



4.6.3 Enclosing the comment
When block comments cover multiple lines, it is only necessary to use the opening and closing comment tokens. This, however, can result in the limits of the comment becoming less than immediately obvious:



/*  Check for all corrupt nodes and add these to the
    Bad Data list. Any clear nodes found are added to the
    Free Data list. */
    CheckNodes( DB_Nodes );



A simple principle that can be used in most cases to clarify the limits of multi-line comments, is to put the closing '*/' directly under the opening '*/' (in a similar manner to braces).



/*  Check for all corrupt nodes and add these to the
    Bad Data list. Any clear nodes found are added to the
    Free Data list.
*/
    CheckNodes( DB_Nodes );



However, reading each line from the left, it is still not immediately clear which line is a comment and which line is not, particularly if the comment is long, and contains blank lines.

Enclosing from the left
In the previous example, you can clearly delimit the comment one line at a time by making the first character that is read an asterisk. This is using the principle of explicitness to say each time, "This is a comment. It is not code."



/*  Check for all corrupt nodes and add these to the
*   Bad Data list. Any clear nodes found are added to the
*   Free Data list.
*/
    CheckNodes( DB_Nodes );



There are several common variant on this, such as putting the opening '/*' on a line by itself, thus ensuring an almost-blank line before the comment and enabling easier line insertion after it. Also, the asterisk may be always put in column two or two asterisks can be used on text lines, to emphasize the comment and to be tidy in having two comment characters per line. Some horizontal space can be saved by using spaces instead of tabs to separate the text from the asterisk:



/*
** Check for all corrupt nodes and add these to the
** Bad Data list. Any clear nodes found are added to the
** Free Data list.
*/
    CheckNodes( DB_Nodes );
/*
 * Alternative comment block format..
 *  ..which puts one asterisk always in column 2
 */



Enclosing from above
An alternative or an addition to white space as a method of distinguishing comments from code is to put a bar above the comment, but not below it. This dissociates the comment from the code above, whilst emphasizing its association with the code below.



/***********************************************************
*   Check for all corrupt nodes and add these to the
*   Bad Data list. Any clear nodes found are added to the
*   Free Data list.
*/
    CheckNodes( DB_Nodes );



Enclosing from below
The comment can be dissociated more from the code below by putting a bar below it too. It is being tidy to keep it the same length as the top line. The dissociation can be further emphasized with a blank line between the comment and the code:



/************************************************************
*   Check for all corrupt nodes and add these to the
*   Bad Data list. Any clear nodes found are added to the
*   Free Data list.
************************************************************/

    CheckNodes( DB_Nodes );



Note that the final '*/' is no longer below the opening '/*'. This is not so important as the limits of the comment block are very clear, although there is a danger of missing the final '/', resulting in the code below being commented out.

A status comment, which describes the code above it, can be enclosed at the bottom, but not the top, to emphasize its association.



/*
*   All open databases have now been closed, with all
*   signs of corruption reported to the corrupt data
*   log. It is now safe to shut the system down.
************************************************************/



Enclosing from the right
The final step is now to tidily fill in the right hand side of the box, although this may be considered to be more trouble than it is worth, as it makes editing the comment text less easy.



/************************************************************
*   Check for all corrupt nodes and add these to the        *
*   Bad Data list. Any clear nodes found are added to the   *
*   Free Data list.                                         *
*************************************************************/



A simplification of the rules about where to place the '/*' and '*/' tokens is to insist that all comments should have matching tokens on the same line. Thus all comment lines are automatically enclosed from the right and the left.



/************************************************************/
/*  Check for all corrupt nodes and add these to the        */
/*  Bad Data list. Any clear nodes found are added to the   */
/*  Free Data list.                                         */
/************************************************************/



With this rule, enclosure from the top and bottom may still be optional. The right hand margin may stay justified or may collapse to a ragged right margin, which eases editing but is not as tidy:



/*  Check for all corrupt nodes and add these to the */
/*  Bad Data list. Any clear nodes found are added to the */
/*  Free Data list. */



4.6.4 Delimiters
Comments need not be used for text comments: they may also be used to separate out distinct pieces of code.

Separating chunks
Drawing lines across the page not only separates the code from the comment, but also separates individual chunks of code, making the chunks easier to see and understand. As these are effectively single-line block comments, they can include simple comments:



/*---- Close all open files ---------------------------------------*/

for ( FileNo = 0; FileNo < NofFilesOpen; FileNo++ )
{
    ErrNo = CloseFile( FileHandle[FileNo] );
    if ( ErrNo != 0 )
    {
        FileError( ErrNo );
    }
}

/*---- Print shutdown message ------------------------------------*/

printf( "System closing down,\n" );
printf( "Remove all tapes and secure in safe.\n");

/*---- Lock terminal off ------------------------------------------*/
...



Multi-line block comments can also a similar scheme, whereby the text in the line is an effective summary for the comment block.



/*---- Check window status -----------------------------------------
*   All windows (including closed ones) must now be checked
*   to ensure all outstanding actions have been completed.
*-------------------------------------------------------------------*/

---------------------------------------------------------------------->

Data/Code delimiters
It can be difficult to immediately find the beginning of the code at the start of a function. For example, a reader might miss the first statement (which may be mistaken for a data declaration).



int
ReadDoorStatus( S_DOOR *Door )

{
int     DoorType;       /* Door construction - WOOD, METAL, etc.    */
int     LockType;       /* Make of lock - CHUBB, YALE, etc.         */
DoorType = WOOD;        /* set default for door construction        */

LockType = Door->Lock;    <------ reader may read code from here!



However, if we put a line across at the start of the data and code sections, no mistakes may be made, and the start of the data and code sections can instantly be found.



int
ReadDoorStatus( S_DOOR *Door )

{
/*---- Data --------------------------------------------------------*/

int     DoorType;       /* Door construction - WOOD, METAL, etc.    */
int     LockType;       /* Make of lock - CHUBB, YALE, etc.         */

/*---- Code --------------------------------------------------------*/

DoorType = WOOD;            /* set default for door construction    */
LockType = Door->Lock;



Delimiter 'weight'
The 'weight' of the delimiter can be used to indicate importance of the section of code or data that is being delimited. The symbols used may be for single line delimiters, or to bound multi-line comment blocks.

A simple scheme would be:

Asterisks (/********/) Major sections, eg. functions, data areas.

Equals (/*======*/) Major sub-sections

Minus (/*------*/) Minor sub-sections

e.g.



/********************************************************************
*    FireOnEnemy( ShipType )
...

/*==== Prepare cannon for firing ===================================*/

/*---- Load cannon -------------------------------------------------*/
...

/*---- Open gun port doors -----------------------------------------*/
...

/*==== Fire and retract cannon =====================================*/
...
'''

expected = '''CHAPTER 4 : Commenting
PART 2 : COMMENTING AND NAMING

CHAPTER 4 : Commenting
4.1 Commenting fundamentals
4.2 Comment types
4.3 Header comments
4.4 File Header comment
4.5 Function header comments
4.6 Block comments
4.7 Trailing comments
4.8 Commenting data
4.9 The preprocessor and comments
4.10 Summary

<--Prev page | Next page -->

4.6 Block comments
Block comments are typically found within functions, between 'chunks' of code. They also appear in other parts of code, for example at the start of chunks of data. There are a number of common approaches to block comments, several of which are discussed below.

4.6.1 Comment size
There are about three different classifications of block comment, depending on its size:

A single line comment will commonly describe a simple item.
A multiple line comment, up to about 5 lines will summarize a more complex item or set of items.
A longer comment will describe even more, although this is now tending towards a major header comment.
Generally, it must be remembered that a block comment has a cost in vertical space and should give value for money. For example, it may be overkill for a block comment to be bigger than the chunk of function code that it describes.

4.6.2 Positioning the comment
A block comment usually describes code below it. This association can be made clearer by using some method to explicitly associate it more closely with the code that it describes.

Using blank lines
A simple principle is to use a blank line above the comment to physically place it closer to the line below than the line above:



    ResetParms();


    for ( Win = 0; Win < NofWins; Win++ )
        CloseWin( Win );



This, however, causes a possible problem where the comment and the code are not immediately distiguishable. A solution, at the cost of more vertical space, is to put a blank line below the comment:



    ResetParms();



    for ( Win = 0; Win < NofWins; Win++ )
        CloseWin( Win );



Indenting the comment
A common method of positioning is to vertically align the comment with the current indent level. This helps to associate the comment with the code below, and preserves the line of indentation. However, this reduces the amount of horizontal space available for comment, particularly at deeper levels of nesting, and may make it more difficult to distinguish between comments and code:



    ResetParms();

    
    for ( Win = 0; Win < NofWins; Win++ )
        CloseWin( Win );



4.6.3 Enclosing the comment
When block comments cover multiple lines, it is only necessary to use the opening and closing comment tokens. This, however, can result in the limits of the comment becoming less than immediately obvious:






    CheckNodes( DB_Nodes );



A simple principle that can be used in most cases to clarify the limits of multi-line comments, is to put the closing '*/' directly under the opening '*/' (in a similar manner to braces).







    CheckNodes( DB_Nodes );



However, reading each line from the left, it is still not immediately clear which line is a comment and which line is not, particularly if the comment is long, and contains blank lines.

Enclosing from the left
In the previous example, you can clearly delimit the comment one line at a time by making the first character that is read an asterisk. This is using the principle of explicitness to say each time, "This is a comment. It is not code."







    CheckNodes( DB_Nodes );



There are several common variant on this, such as putting the opening '/*' on a line by itself, thus ensuring an almost-blank line before the comment and enabling easier line insertion after it. Also, the asterisk may be always put in column two or two asterisks can be used on text lines, to emphasize the comment and to be tidy in having two comment characters per line. Some horizontal space can be saved by using spaces instead of tabs to separate the text from the asterisk:








    CheckNodes( DB_Nodes );







Enclosing from above
An alternative or an addition to white space as a method of distinguishing comments from code is to put a bar above the comment, but not below it. This dissociates the comment from the code above, whilst emphasizing its association with the code below.








    CheckNodes( DB_Nodes );



Enclosing from below
The comment can be dissociated more from the code below by putting a bar below it too. It is being tidy to keep it the same length as the top line. The dissociation can be further emphasized with a blank line between the comment and the code:









    CheckNodes( DB_Nodes );



Note that the final '*/' is no longer below the opening '/*'. This is not so important as the limits of the comment block are very clear, although there is a danger of missing the final '/', resulting in the code below being commented out.

A status comment, which describes the code above it, can be enclosed at the bottom, but not the top, to emphasize its association.











Enclosing from the right
The final step is now to tidily fill in the right hand side of the box, although this may be considered to be more trouble than it is worth, as it makes editing the comment text less easy.











A simplification of the rules about where to place the '/*' and '*/' tokens is to insist that all comments should have matching tokens on the same line. Thus all comment lines are automatically enclosed from the right and the left.











With this rule, enclosure from the top and bottom may still be optional. The right hand margin may stay justified or may collapse to a ragged right margin, which eases editing but is not as tidy:









4.6.4 Delimiters
Comments need not be used for text comments: they may also be used to separate out distinct pieces of code.

Separating chunks
Drawing lines across the page not only separates the code from the comment, but also separates individual chunks of code, making the chunks easier to see and understand. As these are effectively single-line block comments, they can include simple comments:





for ( FileNo = 0; FileNo < NofFilesOpen; FileNo++ )
{
    ErrNo = CloseFile( FileHandle[FileNo] );
    if ( ErrNo != 0 )
    {
        FileError( ErrNo );
    }
}



printf( "System closing down,\n" );
printf( "Remove all tapes and secure in safe.\n");


...



Multi-line block comments can also a similar scheme, whereby the text in the line is an effective summary for the comment block.








---------------------------------------------------------------------->

Data/Code delimiters
It can be difficult to immediately find the beginning of the code at the start of a function. For example, a reader might miss the first statement (which may be mistaken for a data declaration).



int
ReadDoorStatus( S_DOOR *Door )

{
int     DoorType;       
int     LockType;       
DoorType = WOOD;        

LockType = Door->Lock;    <------ reader may read code from here!



However, if we put a line across at the start of the data and code sections, no mistakes may be made, and the start of the data and code sections can instantly be found.



int
ReadDoorStatus( S_DOOR *Door )

{


int     DoorType;       
int     LockType;       



DoorType = WOOD;            
LockType = Door->Lock;



Delimiter 'weight'
The 'weight' of the delimiter can be used to indicate importance of the section of code or data that is being delimited. The symbols used may be for single line delimiters, or to bound multi-line comment blocks.

A simple scheme would be:

Asterisks () Major sections, eg. functions, data areas.

Equals () Major sub-sections

Minus () Minor sub-sections

e.g.

















'''


def test_strips_c():

    assert strip.strip(source, language='c', preserve_newlines=True) == expected
