<?php
$key=''
$location='经度,纬度'


$updat = $_GET["update"];
$datea = date('Ymd');
$datea = './weather/'.$datea.'.json';
if(file_exists($datea) || $updat == true)
{
    $handle = fopen($datea, "r");
    $contents = fread($handle, filesize ($datea));
    fclose($handle);
    echo $contents;
}
if(!file_exists($datea))
{
    $url = "https://devapi.qweather.com/v7/weather/now?key="+$key+"&location="+$location; 
    $html = file_get_contents("compress.zlib://".$url); 
    echo $html;
    touch($datea);
        $CONFIGfile = fopen($datea, "w");
        $txt =$html;
        fwrite($CONFIGfile, $txt);
        fclose($CONFIGfile);
}



?>
