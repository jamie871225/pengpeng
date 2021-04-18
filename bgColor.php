<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign In</title>

    <style type="text/css">
    /* http://meyerweb.com/eric/tools/css/reset/ 
    v2.0 | 20110126
    License: none (public domain)
    */

    html, body, div, span, applet, object, iframe,
    h1, h2, h3, h4, h5, h6, p, blockquote, pre,
    a, abbr, acronym, address, big, cite, code,
    del, dfn, em, img, ins, kbd, q, s, samp,
    small, strike, strong, sub, sup, tt, var,
    b, u, i, center,
    dl, dt, dd, ol, ul, li,
    fieldset, form, label, legend,
    table, caption, tbody, tfoot, thead, tr, th, td,
    article, aside, canvas, details, embed, 
    figure, figcaption, footer, header, hgroup, 
    menu, nav, output, ruby, section, summary,
    time, mark, audio, video {
        margin: 0;
        padding: 0;
        border: 0;
        font-size: 100%;
        font: inherit;
        vertical-align: baseline;
    }
    /* HTML5 display-role reset for older browsers */
    article, aside, details, figcaption, figure, 
    footer, header, hgroup, menu, nav, section {
        display: block;
    }
    body {
        line-height: 1.5;
    }
    ol, ul {
        list-style: none;
    }
    blockquote, q {
        quotes: none;
    }
    blockquote:before, blockquote:after,
    q:before, q:after {
        content: '';
        content: none;
    }
    table {
        border-collapse: collapse;
        border-spacing: 0;
    }
    img{
        max-width:100%;
        height:auto;
    }
    *,*::before,*::after{
        box-sizing:border-box;
    }
    /* CSS reset END */
    .pure-form input[type="text"],
    .pure-form input[type="password"]{
        padding: 0.8em;
        display: inline-block;
        border: 1px solid #ccc;
        box-shadow: inset 0 1px 3px #ddd;
        border-radius: 4px;
        vertical-align: middle;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
        margin-bottom:0.6em;
        font-size:14px;
        width:300px;
    }
    .pure-form input[type="text"]:focus,
    .pure-form input[type="password"]:focus{
        outline: 0;
        border-color:rgb(211, 86, 103);
    }
    .pure-form input:not([type]):focus {
        outline: 0;
        border-color:rgb(211, 86, 103);
    }
    .pure-form label{
        font-size:18px;
    }
    /* Pure form END */

    .pure-button {
        /* Structure */
        display: inline-block;
        zoom: 1;
        line-height: normal;
        white-space: nowrap;
        vertical-align: middle;
        text-align: center;
        cursor: pointer;
        -webkit-user-drag: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
    }
    .pure-button {
        font-size: 16px;
        margin-top:1em;
        padding: 0.7em;
        color: white;
        border: 1px solid #999;  /*IE 6/7/8*/
        border: none rgba(0, 0, 0, 0);  /*IE9 + everything else*/
        background-color: rgb(234, 168, 176);
        text-decoration: none;
        border-radius: 3px;
    }
    .pure-button:focus {
        outline: 0;
    }
    .pure-button:hover{
        background-color:rgb(236, 186, 192);
    }
    /* Pure button END */

    body{
        font-family:Helvetica;
        color:rgb(65, 54, 54);
        background-color:rgb<?php echo $bgColor; ?>;
    }
    .login{
        display:flex;
        justify-content:center;
        padding-top:120px;
        padding-bottom:120px;
    }
    .wrap{
        padding:30px 25px;
        text-align:center;
        display:inline-block;
        background-color:white;
        border-radius:5px;
        box-shadow:0px 5px 20px rgb(210, 210, 210);
    }
    .login h1{
        color:rgb(211, 86, 103);
        font-size:24px;
        padding:0px 0px 10px 0px;
        font-weight:bold;
    }
    .form-login .account, .form-login .password, .form-login{
        display:flex;
        flex-direction:column;
        text-align:left;
    }
    .form-login label{
        font-size:16px;
        margin:8px 0px 3px 0px;
    }
    .pass-register{
        text-align:right;
        margin-top:10px;
        color:rgb(65, 54, 54);
    }
    .pass-register a{
        text-decoration:none;
        font-size:14px;
        color:rgb(65, 54, 54);
    }
    .pass-register a:hover{
        color:rgb(211, 86, 103);
    }
    .pass-register p{
        display:inline-block;
        font-size:12px;
        font-weight:bold;
    }
    </style>
    <?php
    $bgColorR=rand(0, 255);
    $bgColorG=rand(0, 255);
    $bgColorB=rand(0, 255);
    $bgColor="($bgColorR, $bgColorG, $bgColorB)";
    ?>
</head>
<body>
    <section class="login">
        <div class="wrap">
            <h1>- Log In -</h1>
            <form action="/signin" class="pure-form form-login" method="POST">
                <div class="account">
                    <label for="account">帳號</label>
                    <input type="text" name="account" id="account" placeholder="使用者名稱">
                </div>
                <div class="password">
                    <label for="password">密碼</label>
                    <input type="password" name="password" id="password" placeholder="8~16位英文、數字">
                </div>
                <button class="pure-button">登入</button>
                <div class="pass-register">
                    <a href="#">忘記密碼 </a>
                    <p>｜</p>
                    <a href="/register"> 註冊</a>
                </div>
            </form>
        </div>
    </section>
</body>
</html>