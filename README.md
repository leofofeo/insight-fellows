# This is my project submission for the Insight Fellows application.

## The project is structured as specified in the assignment README

The bulk of my work exists in the `src` directory. There are three main
directories there - `models`, `processing`, and `utils`. Additionally, `main.py` 
exists at the root of `src` and calls the two main processing functions with the 
path to the appropriate folders. 

## Models

The models directory contains three files with classes representing
the structure of the data throughout the parsing and processing. 

The most notable ones are `Product`, `ProductNames`, and `Companies`. `Product` does the bulk of the work - a `Product` class is instantiated when a new combination of `Product.name` and `Product.year` are found. This unique combination is the demarcation point for each output row, so `Product` serves as an aggregator to keep track of information coming in from the input file.

`ProductNames` is a helper class primarily meant to keep track of acceptable
Product names. I made the decision early on to truncuate a product's name for readability throughout the parsing. On reflection, this doesn't need to be in the program, but I've left it in for future extensibility.

The `Companies` class is a compositional class that serves as an attribute for `Product`. I wrote the class to help manage the data gathering for specific companies and their corresponding complaints. The biggest benefit to using this class was the ability down the line to identify which companies had received the most complaints (which proved unnecessary after re-reading the assignment prompt), and can presently be used as a substitute for some of the `Product` calculations when printing out the row. I left a comment in the class about this, and decided to stick with the class to show the relationship between the different segments of data that we're outputting.

`OutputRow` was written in anticipation of needing to do something fancy while writing to a csv and proved unnecessary. I've left it in for posterity, and because a more developed or intricate project might well need a similar blueprint.


## Utils

The `utils` directory contains one module, `utils`, which itself contains three helper methods. These methods are straightforward and exist to compartmentalize operations that require error handling or that use some sort of function or method chaining that decreases readability.


## Processing

The processing directory contains one file with two methods, `process_csv_input` and `process_csv_output`. The former does the bulk of the work. It iterates over every row in the csv, and as it goes does the proper error handling with the cells that require capture. It creates and updates instantiated `Product` objects to keep track of the data coming through, and then returns a dictionary with a unique year-name combination as its key to segment products appropriately. It makes heavy use of helper functions to keep the business logic as clean as possible.

`process_csv_output` is much more straightforward. It accepts the returned dictionary of `{"yearname": Product}` key-value pairs, turns it into an ordered list (alphabetically, and then by year), and then iterates over each `Product` in the list. `Products` contain all the necessary information for the output cell, so this function writes to each row accordingly as it iterates.


## Tests

Tests in the `test` directory test the program in a couple of ways. They're structured to mirror the directories in `src`, and test each object and helper method's ability to do its job. Additionally, a couple of different tests test the actual input and output functionality of the program, using a variety of `assert` statements to confirm that the `process_` methods are doing what they should. In a way, these can be viewed as end-to-end tests, especially since they use the same test data as the main program.
