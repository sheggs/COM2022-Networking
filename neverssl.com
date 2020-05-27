HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1416
Connection: close
Last-Modified: Thu, 06 Jun 2019 04:19:28 GMT
Accept-Ranges: bytes
Server: AmazonS3
Date: Tue, 26 May 2020 02:04:49 GMT
ETag: "92b6819fcf2865f6be341e02390d23bf"
Vary: Accept-Encoding
X-Cache: Hit from cloudfront
Via: 1.1 d31be1bb3cd2f187c0f45c1f03ead3c6.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: LHR3-C2
X-Amz-Cf-Id: g-lEYtjgXL_WOIDNkLARhep6Ui99BSE1wUlwZHsu-IYAb1pCBG8b9A==
Age: 51596

<html>
    <head>
        <title>NeverSSL - Connecting ... </title>

        <style>
        body {
             font-family: Montserrat, helvetica, arial, sans-serif; 
             font-size: 16x;
             color: #444444;
             margin: 0;
        }
        h2 {
            font-weight: 700;
            font-size: 1.6em;
            margin-top: 30px;
        }
        p {
            line-height: 1.6em;
        }
        .container {
            max-width: 650px;
            margin: 20px auto 20px auto;
            padding-left: 15px;
            padding-right: 15px
        }
        .header {
            background-color: #42C0FD;
            color: #FFFFFF;
            padding: 10px 0 10px 0;
            font-size: 2.2em;
        }
        <!-- CSS from Mark Webster https://gist.github.com/markcwebster/9bdf30655cdd5279bad13993ac87c85d -->
        </style>

        <script>
            var prefix = 'bcdfhklmnrstvwxz';
            
            prefix = prefix.split('').sort(function(){return 0.5-Math.random()}).join('')

            window.location.href = 'http://' + prefix + '.neverssl.com/online'; 
        </script>
    </head>
    <body>

    <div class="header">
        <div class="container">
        <h1>NeverSSL</h1>
        </div>
    </div>
    
    <div class="content">
    <div class="container">

    <h1>Connecting ...</h1>

    </div>
    </div>
    
    </body>
</html>
