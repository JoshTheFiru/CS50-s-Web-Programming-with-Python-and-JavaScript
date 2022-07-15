<!-- HTML SECTION -->

# CHAPTER 0 - HTML, CSS

## HTML

**DOCTYPE declaration** -> Tells the browser what version of HTML we're using.

    <!DOCTYPE html> --> Version 5 of HTML

**DOM** -> Document Object Model: Tree-like structure that describes
how all the HTML elements are related to each other.

**DATALISTS**:
    New to html5 it allows to create a dropdown that filters really quickly and that divides in two parts:
    an input and a datalist both referenced to each other by putting the same value in the input's list attribute, and the datalist's id.

        <div>
            <input name="country" list="countries" placerholder="Country">
            <datalist id="countries">
                <option value="Afghanistan">
                <option value="Afghanistan">
                <option value="Afghanistan">
                <option value="Afghanistan">
            </datalist>
            </input>
        </div>

## CSS

**CSS Selectors**:
|Elements| Type of Selector         |
|------:|--------------------------:|
|  a, b | Multiple Element Selector |
|  a b  | Descendant Selector       |
| a > b | Child Selector            |
| a + b | Adjacent Sibling Selector |
| [a=b] | Attribute Selector        |
| a:b   | Pseudoclass Selector      |
| a::b  | Pseudoelement Selector    |

**Descendant Selector & Child Selector**: Selects the child of the element firstly referenced.

    <ol>
        <li>Item 1</li>
        <li>Item 2</li>
        <ul>
            <li>Subitem 1</li>
            <li>Subitem 2</li>
        </ul>
        <li>Item 3</li>

If I would want to style only the Subitems, I could do in the css

    ul li{
        color: blue
    }

Or to do the same thing, as they are equivalent:

    ul > li{ 
        color: blue
    }

**Pseudoclass & Pseudoelement Selector**: Type of selector that only styles when an element enters on a determined state (ergo, has some pseudoclass like hover)

    button:hover{
        color: red; 
    }

Only styles when the button has been hovered.

## Responsive Design

**vieport**: The viewport is the visual part of the screen that the user can actually see.

*IN ORDER FOR THE PAGE TO ADAPT, ONE SIMPLE THING WE CAN DO IS JUST TO ADD A LITTLE LINE OF CODE TO THE HTML INSIDE THE HEAD SECTION OF THE PAGE THAT CONTROLS THE VIEWPORT.*

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

We are telling the page to be as wide as the device width.

In addition to tihs, there exist the media queries

**Media Queries**: They control how the page look like depending on different factors (size of the screen, type of browser,...).

    @media (min-width: 600px) { //any viewport of larger or equal to 600px
        body{
            background-color: black; 
        }
    }

    @media (max-width: 599px) { //any viewport of smaller or equal to 599px
        body{
            background-color: red; 
        }
    }

**Flexbox**: If we have multiple elements that might overflow if we're not careful about how we do responsive design, is where flexbox comes in really handy.

You need to tell the container element (or one which contains / wraps the elements you want to apply flexbox to), to be flexbox by:

    #container{
        display: flex
    }

This way, everything inside the container will have flexbox applied.

Flexbox is a modern paradigm layout, but there are others (we can say Media Queries is another layout paradigm).

**Grid**: Grid is another layout paradigm that as Flexbox does, styles and adapts a design, depending on the device vieport's width:

    #container{
        display: grid
        grid-column-gap: 20px;  //How much space I want between columns
        grid-row-gap: 10px;     //How much space I want between rows
        grid-template-columns: 200px 200px auto; //I will have 3 columns,first and second with 200px width and third that will rescale automatically depending on the viewport
    }

## Bootstrap

Bootstrap's column model divides its page into 12 distinct columns. It divides every row into 12 column units, so with a class like

    "<div class="col-3"> This is a 3 column width section </div>

I am giving this div component a 3 column width, and I would still have another 9 column units to insert more elements in that specific row. This layout paradigm will be fully responsive and will shrink as the viewport does. Of course, the columns in a row will not need to be the same size.

Bootstrap also allows to specify the amount of columns taken by an element depending on the size of the screen.

    <div class="row">
        <div class="col-lg-3 col-sm-6">This is a section </div>
    </div>

This row will display an element that will take 3 column units space in a large screen, and 6 column units space in a small screen.

## Sass

Extesnion to CSS, it allows to use and manipulate CSS in a way that is going to be faster and remove some of the repetition that we might have in plain CSS.

One of the key features of Sass is the ability to have variables. As Sass is a different language, it requires a different extension for its files, which is .scss.

All variables start with the $ character:

    $color: red; //Creates a variable called color, which value is red. 

Then, we apply it to the element as:

    element{
        color: $color; 
    }

It's important to notice that while web browsers understand CSS, they can't by default understand Scss, or Sass. In order to solve this, once the file is written, we need to compile it, convert it, translate it, from Sass into plain old CSS. In order to do all this, you need to install Sass in your machine, and then in the terminal:

    sass fileName.scss:fileName.css

To avoid recompiling the file everytime you make a change, you can automate the process, by stating on the terminal:

    sass --watch variables.scss:variables.css

Also you can do this not just with single files, but entire directories as well if you have multiple different Sass files.

Apart from these, Sass gives the ability to nest CSS selectors inside of other CSS selectors, simplifying the process to target elements:

    element{
        attribute: value;
        attribute: value;

        subelement{
            attribute: value;
            attribute: value;
        }

        subelement{
            attribute: value;
            attribute: value;
        }
    }

Sass also offers inheritance. If we have certain CSS selectors that are related to other CSS selectors, but they're may be adding some additional information.

So, the generic element properties will be defined by using a *%name*, and child elements will extend that:

    %parent{
        attribute: value;
        attribute: value;
    }

    child{
        extend: %parent;        //It receives the attributes and values from the parent
        attribute: value;
        attribute: value;
    }
