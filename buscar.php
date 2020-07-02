<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    $itens = glob('/home/ph/Vídeos/*.mp4');
    if ($itens !== false) {
        foreach ($itens as $item) {
            echo $item.'<br />';
        }
    }
    ?>
</body>
</html>