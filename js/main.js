var curIndex = 0;
//时间间隔 单位毫秒
var timeInterval = 2000;
var array = new Array ();
array[0] ="./img/img1.jpg";
array[1] ="./img/img2.jpg";
array[2] ="./img/img3.jpg";
array[3] ="./img/img4.jpg";
array[4] ="./img/img5.jpg";
array[5] ="./img/img6.jpg";
setInterval(changeImg,timeInterval);
function changeImg() {
    var obj = document.getElementById("img");
    if(curIndex == array.length-1) {
        curIndex = 0;
    } else {
        curIndex++;
    }
    obj.src = array[curIndex];
}
