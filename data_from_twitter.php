
\\\**TWITTER DATA IN JSON FROMAT**///


<?php
require_once('include/TwitterAPIExchange.php');
require_once('include/OAuth.php');
require_once('include/twitteroauth.php');
$settings = array(
'consumer_key' =>"XXXXXXXXXXXXXXXXXXXXXX",
'consumer_secret' => "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
'oauth_access_token' =>"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
'oauth_access_token_secret' =>"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
);
$requestMethod='GET';
$url='https://api.twitter.com/1.1/statuses/user_timeline.json';
$getfield = '?screen_name=poojaaaa&count=10';
$twitter= new TwitterAPIExchange($settings);
$response = $twitter ->setGetfield($getfield)
->buildOauth($url,$requestMethod)
->performRequest();
echo "$response";
?>
