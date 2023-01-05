

    //以下的_is是_intersect的缩写
    var array_is_text;
    function init_intersect(){
        // 初始化两个div的高度
        $("#div_is_inner").css({"height":$(window).height()+"px"});
        $(".div_is_typed").css({"height":$(window).height()+"px"});
        $(".div_is_open_bg").css({"height":$(window).height()+"px"});

        //设置自定义背景
        $("#div_intersect").css({"height":$(window).height()+"px"});
        var start_bg_img=start_content['bg_img'];
        if(typeof(start_content['bg_style'])!='undefined' && start_content['bg_style']=='bg_custom'){
            if(typeof(start_bg_img)!='undefined' && start_bg_img!=''){
                $("#div_intersect").css({"background-image": 'url('+start_bg_img+')'});
            }
        }

        var intersect_text=start_content['intersect_text'];
        if(typeof(intersect_text)!='undefined' && intersect_text!=''){
            array_is_text=[intersect_text];  //加载自定义内容
        }else{  //设置默认值
            array_is_text=['我知道遇见你不容易，错过会很可惜，我不希望余生都是回忆，我想余生每天都是你，我爱你。'];
            // array_str_temp=[];
            // random_text_array(array_str_temp,3);
            // array_is_text[0]=array_is_text[0]+'<br>'+array_str_temp.join('<br>');
            console.log(array_is_text);
        }
    }

    function init_is_typed(){
        $(".div_is_open_bg").fadeOut("slow"); //隐藏初始bg

        // 设置正文之前的照片
        var img_src=start_content['img_src'];
        if(typeof(start_content['img_bool'])!='undefined' && start_content['img_bool']=='img_true'){ //如果设置了照片
            if(typeof(img_src)!='undefined' && img_src!=''){
                $("#div_is_img").fadeIn("slow"); //
                $("#div_is_img .img_is_typed").attr('src',img_src); //
            }
        }
        if(typeof(start_content['img_bool'])=='undefined' || typeof(start_content['intersect_text'])=='undefined'){
            var random_img=random_img_as();
            $("#div_is_img").fadeIn("slow"); //
            $("#div_is_img .img_is_typed").attr('src',random_img); //
        }

        //以下是打字效果的js
        var str_cursorChar;
        if(typeof(start_content['cursor_char'])!='undefined' && start_content['cursor_char']!=''){
            switch(start_content['cursor_char']){ //设置打字光标的样式
                case 'cursor_heart':
                    str_cursorChar='❤';
                    break;
                case 'cursor_sub':
                    str_cursorChar='_';
                    break;
                case 'cursor_music':
                    str_cursorChar='♫';
                    break;
                case 'cursor_star':
                    str_cursorChar='★';
                    break;
                case 'cursor_sun':
                    str_cursorChar='☀';
                    break;
                default:
                    str_cursorChar='|';
            }
        }else{
            str_cursorChar='❤';
        }

        var typed_intersect = new Typed('#span_is_typed', {
            strings: array_is_text, //输入内容, 支持html标签
            typeSpeed: 150, //打字速度
            // backSpeed: 50, //回退速度
            // backDelay: 1000,
            loop: false, //要不要循环
            cursorChar: str_cursorChar,//替换光标的样式
            contentType: 'html', //值为html时，将打印的文本标签直接解析html标签
            onComplete: function(abc){
                        console.log(abc);
                        console.log('finished typing words');
                        setTimeout(function(){
                            init_theme();
                            $('#div_intersect').remove();
                        },2000);
                    },
        });
    }

    function random_text_array(temp_array,length){  //获取随机的模板图片
        console.log('random_text_array');
        var random_array=[];
        while(random_array.length<length){
            // var random_num=Math.floor(Math.random()*(array_as_pics.length-0))+0;
            var random_num=Math.floor(Math.random()*(array_as_words_love.length)); //随机取值
            if(random_array.indexOf(random_num)==-1){
                random_array.push(random_num);
            }
        }
        // console.log(random_array);
        for(var i=0; i<length; i++){
            temp_array.push(array_as_words_love[random_array[i]]); //获取随机的模板图片
        }
    }

    function random_img_as(){  //获取随机的模板图片
        // console.log('random_img_as');
        var random_num=Math.floor(Math.random()*(array_as_pics_s.length)); //随机取值
        var random_img=array_as_pics_s[random_num];
        return random_img;
    }




    // 这是画布动画背景的js
    var canvas_is = document.getElementById("canvas_is");
    var ctx_is = canvas_is.getContext("2d");
    //设置画布的大小
    var cw_is = canvas_is.width = window.innerWidth,
        cx = cw_is / 2;
    var ch_is = canvas_is.height = window.innerHeight,
        cy = ch_is / 2;

    ctx_is.fillStyle = "#483D8B"; //这个似乎没有用？？
    var linesNum = 25; //线条的数量
    var linesRy = [];  //
    var requestId = null;

    for (var i = 0; i < linesNum; i++) {
        var flag = i % 2 == 0 ? "h" : "v";
        var l = new Line_is(flag);
        linesRy.push(l);
    }

    setTimeout(function () {
        Init_is();
        addEventListener('resize', Init_is, false);
    }, 15);


    // 画线
    function Line_is(flag) {
        this.flag = flag;
        this.a = {};
        this.b = {};

        if (flag == "v") {
            this.a.y = 0;
            this.b.y = ch_is;
            this.a.x = randomIntFromInterval(0, ch_is);
            this.b.x = randomIntFromInterval(0, ch_is);
        } else if (flag == "h") {
            this.a.x = 0;
            this.b.x = cw_is;
            this.a.y = randomIntFromInterval(0, cw_is);
            this.b.y = randomIntFromInterval(0, cw_is);
        }

        this.va = randomIntFromInterval(25, 100) / 100;
        this.vb = randomIntFromInterval(25, 100) / 100;

        this.draw = function () {
            ctx_is.strokeStyle = "#D8BFD8"; //线条的颜色
            ctx_is.beginPath();
            ctx_is.moveTo(this.a.x, this.a.y);
            ctx_is.lineTo(this.b.x, this.b.y);
            ctx_is.stroke();
        }

        this.update = function () {
            if (this.flag == "v") {
                this.a.x += this.va;
                this.b.x += this.vb;
            } else if (flag == "h") {
                this.a.y += this.va;
                this.b.y += this.vb;
            }
            this.edges();
        }

        this.edges = function () {
            if (this.flag == "v") {
                if (this.a.x < 0 || this.a.x > cw_is) {
                    this.va *= -1;
                }
                if (this.b.x < 0 || this.b.x > cw_is) {
                    this.vb *= -1;
                }
            } else if (flag == "h") {
                if (this.a.y < 0 || this.a.y > ch_is) {
                    this.va *= -1;
                }
                if (this.b.y < 0 || this.b.y > ch_is) {
                    this.vb *= -1;
                }
            }
        }
    }

    function Draw_is() {
        requestId = window.requestAnimationFrame(Draw_is);
        ctx_is.clearRect(0, 0, cw_is, ch_is);

        for (var i = 0; i < linesRy.length; i++) {
            var l = linesRy[i];
            l.draw();
            l.update();
        }
        for (var i = 0; i < linesRy.length; i++) {
            var l = linesRy[i];
            for (var j = i + 1; j < linesRy.length; j++) {
                var l1 = linesRy[j]
                Intersect2lines(l, l1);
            }
        }
    }

    function Init_is() {
        linesRy.length = 0;
        for (var i = 0; i < linesNum; i++) {
            var flag = i % 2 == 0 ? "h" : "v";
            var l = new Line_is(flag);
            linesRy.push(l);
        }
        if (requestId) {
            window.cancelAnimationFrame(requestId);
            requestId = null;
        }
        // cw_is = canvas_is.width = window.innerWidth,
        cw_is = canvas_is.width = 500,
                cx = cw_is / 2;
        ch_is = canvas_is.height = window.innerHeight,
                cy = ch_is / 2;
        Draw_is();
    }

    function Intersect2lines(l1, l2) {
        var p1 = l1.a,
            p2 = l1.b,
            p3 = l2.a,
            p4 = l2.b;
        var denominator = (p4.y - p3.y) * (p2.x - p1.x) - (p4.x - p3.x) * (p2.y - p1.y);
        var ua = ((p4.x - p3.x) * (p1.y - p3.y) - (p4.y - p3.y) * (p1.x - p3.x)) / denominator;
        var ub = ((p2.x - p1.x) * (p1.y - p3.y) - (p2.y - p1.y) * (p1.x - p3.x)) / denominator;
        var x = p1.x + ua * (p2.x - p1.x);
        var y = p1.y + ua * (p2.y - p1.y);
        if (ua > 0 && ub > 0) {
            markPoint({
                x: x,
                y: y
            })
        }
    }

    // 生成相交点
    function markPoint(p) {
        ctx_is.beginPath();
        ctx_is.fillStyle = "#DDA0DD"; //相交点的颜色
        ctx_is.arc(p.x, p.y, 2, 0, 2 * Math.PI);
        ctx_is.fill();
    }

    function randomIntFromInterval(mn, mx) {
        return ~~(Math.random() * (mx - mn + 1) + mn);
    }