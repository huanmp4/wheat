function Orderedit(){

}

Orderedit.prototype.uploadPicture = function(){
    var img = $(".imagedown0");
    var inp = $(".hideInput");
    img.click(function(){
        inp.click();
        inp.change(function(){
            console.log("1111:");
            var file = this.files[0];
            var formdata = new FormData();
            formdata.append("file",file);
            console.log("file:",formdata);
            xfzajax.post({
                "url":"/imageupdata",
                "data":formdata,
                "contentType":false,
                "processData":false,
                "success":function(e){
                    if(e.code === 200){
                        var url = e.data;
                        img.attr("src",url)
                    }else{
                        console.log("图片上传错误")
                    }
                }
            })
        })
    })
};

Orderedit.prototype.editOrder = function(){
    var BTN = $("#submitBTN-order-edit");
    BTN.click(function(){
        var table = $(".formTables");
        var orderid = $(this).attr("data-order-id");
        var pic = table.find(".imagedown0").attr("src");
        var shop = table.find("input[name='shop']").val();
        var fare = table.find("input[name='fare']").val();
        var num = table.find("input[name='num']").val();
        var standarsname = table.find("input[name='standarsname']").val();
        var status = table.find("select[name='status']").val();
        // console.log("orderid:",orderid);
        // console.log("pic:",pic);
        // console.log("shop:",shop);
        // console.log("fare:",fare);
        // console.log("num:",num);
        // console.log("standarsname:",standarsname);
        // console.log("status:",status);
        xfzajax.post({
            "url":"/orderupdate",
            "data":{
                "orderid":orderid,
                "pic":pic,
                "shop":shop,
                "fare":fare,
                "num":num,
                "standarsname":standarsname,
                "status":status
            },
            "success":function(e){
                if (e.code === 200){
                    xfzalert.alertSuccess("修改成功")
                }else{
                    xfzalert.alertError("修改失败")
                }
            }
        })



    })
};

Orderedit.prototype.Run = function(){
    var self = this;
    self.editOrder();
    self.uploadPicture();


};



$(function(){
    var edit = new Orderedit();
    edit.Run()
});