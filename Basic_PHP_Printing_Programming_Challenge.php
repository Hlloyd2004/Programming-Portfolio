<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic PHP Printing Programming Challenge:</title>
</head>
<body>
    <form action="Basic PHP Printing Programming Challenge.php" method="get">
        <input type="text" name="slug">
        <input type="submit">
<!-- This form is used so that the user doesn't need to edit the URL bar -->
    </form>
    <?php
        $slug = $_GET ["slug"];
        $arr=array("Welcome home" => "home", 
            "Learn more about what we do" => "about-us",
            "Feel free to get in touch with us" => "contact-us");
    // This is the array that includes the different slugs.
?>
<!--This array search looks through the $arr array 
using the variable $slug -->
    <h1><?php echo array_search ($slug, $arr);?></h1>
<!-- Using this H1 tag i have displayed the 
results in a larger font to the screen -->


</body>
</html>