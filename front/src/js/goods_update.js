function _Goods(){
    this.closeBTN = $(".closeBTN");
    this.closeBTN1 = $(".closeBTN1");

    this.file0 = $(".file0");
    this.file1 = $(".file1");
    this.file2 = $(".file2");
    this.file3 = $(".file3");
    this.file4 = $(".file4");
    this.file5 = $(".file5");
    this.imagedown0 = $(".imagedown0");
    this.imagedown1 = $(".imagedown1");
    this.imagedown2 = $(".imagedown2");
    this.imagedown3 = $(".imagedown3");
    this.imagedown4 = $(".imagedown4");
    this.imagedown5 = $(".imagedown5");
}



_Goods.prototype.uploadImages = function(){
    var self = this;
    self.imagedown0.click(function(e){
        e.preventDefault();
        self.func({"1":self.file0,"2":self.imagedown0});
    });
    self.imagedown1.click(function(e){
        e.preventDefault();
        self.func({"1":self.file1,"2":self.imagedown1});
    });
    self.imagedown2.click(function(e){
        e.preventDefault();
        self.func({"1":self.file2,"2":self.imagedown2});
    });
    self.imagedown3.click(function(e){
        e.preventDefault();
        self.func({"1":self.file3,"2":self.imagedown3});
    });
    self.imagedown4.click(function(e){
        e.preventDefault();
        self.func({"1":self.file4,"2":self.imagedown4});
    });
    self.imagedown5.click(function(e){
        e.preventDefault();
        self.func({"1":self.file5,"2":self.imagedown5});
    });

};


_Goods.prototype.func = function(e){
    var file = e["1"];
    var img = e["2"];
    console.log("e:",e);
    file.click();
    file.change(function(){
        var file = this.files[0];
        var formdata = new FormData();
        formdata.append("file",file);
        xfzajax.post({
            "url":"/imageupdata",
            "data":formdata,
            "processData":false,
            "contentType":false,
            "success":function(e){
                console.log("e",e);
                if (e.code === 200){
                    var url = e.data;
                    img.attr("src",url);
                    img.attr("data-url",url);
                }else{
                    console.log("图片上传给服务器回调失败")
                }
            }
        })
    })
};



_Goods.prototype.onClickEvent = function(){
    var self = this;
    self.closeBTN.click(function(){
        console.log("关闭按钮");
        var id = $(this).attr("data-goodid");
        console.log("data-goodid:",id);
        xfzalert.alertConfirm({
            "title":"确定要删除吗?",
            "confirmCallback":function(){
                xfzajax.post({
                    "url":"/delete",
                    "data":{"id":id},
                    "success":function(e){
                        if(e.code === 200){
                            window.location.reload()
                        }
                    }
                })
            }
        })
    })
};

_Goods.prototype.closeEventBTN = function(){
    var self = this;
    self.closeBTN1.click(function(){
        $(".shell").css("visibility","hidden");
    })
};


_Goods.prototype.edit = function(){
    var edit = $(".btn-edit");
    edit.click(function(e){
        e.preventDefault();
        var good_id = $(this).attr("data-goodid");
        console.log("edit",good_id);
        xfzajax.post({
            "url":"/edit",
            "data":{"id":good_id},
            "success":function(e){
                if(e.code === 200){
                    var data = e.data;
                    var shell = $(".shell");
                    data.toppicture = eval(data.toppicture);
                    shell.css("visibility","visible");
                    shell.find('.imagedown0').attr("src",data.detail);
                    shell.find('.imagedown5').attr("src",data.shoplogo);
                    shell.find('.imagedown1').attr("src",data.toppicture[0]);
                    shell.find('.imagedown2').attr("src",data.toppicture[1]);
                    shell.find('.imagedown3').attr("src",data.toppicture[2]);
                    shell.find('.imagedown4').attr("src",data.toppicture[3]);
                    shell.find('input[name="name"]').val(data.name);
                    shell.find('input[name="price"]').val(data.price);
                    shell.find('input[name="fare"]').val(data.fare);
                    shell.find('input[name="shop"]').val(data.shop);
                    shell.find('input[name="standars"]').val(data.standars);
                    shell.find(".closeBTN1").attr("data-goodid",data.id)
                }
            }
        })
    })
};


_Goods.prototype.submitEditer = function(){
    var self = this;
    var submit_edit = $(".btn-edit-confirm");
    submit_edit.click(function(){
        var shell = $(".shell");
        var good_id = shell.find('.closeBTN1').attr("data-goodid");
        var file_p0 = shell.find('.imagedown0').attr("src");
        var file_p1 = shell.find('.imagedown1').attr("src");
        var file_p2 = shell.find('.imagedown2').attr("src");
        var file_p3 = shell.find('.imagedown3').attr("src");
        var file_p4 = shell.find('.imagedown4').attr("src");
        var file_p5 = shell.find('.imagedown5').attr("src");
        var name = shell.find('input[name="name"]').val();
        var price = shell.find('input[name="price"]').val();
        var fare = shell.find('input[name="fare"]').val();
        var shop = shell.find('input[name="shopName"]').val();
        var standars = shell.find('input[name="standars"]').val();
        console.log("good_id",good_id);
        console.log("file_p0",file_p0);
        console.log("file_p1",file_p1);
        console.log("file_p2",file_p2);
        console.log("file_p3",file_p3);
        console.log("file_p4",file_p4);
        console.log("file_p5",file_p5);
        console.log("name",name);
        console.log("price",price);
        console.log("fare",fare);
        console.log("shop",shop);
        console.log("standars",standars);
        xfzajax.post({
            "url":"/goods_update",
            "data":{
                "good_id":good_id,
                "file_p0":file_p0,
                "file_p1":file_p1,
                "file_p2":file_p2,
                "file_p3":file_p3,
                "file_p4":file_p4,
                "file_p5":file_p5,
                "name":name,
                "fare":fare,
                "price":price,
                "shop":shop,
                "standars":standars
            },
            "success":function(e){
                if (e.code ===200){
                    console.log("ok");
                    window.location.reload();
                    xfzalert.alertSuccess("修改成功")
                }

            }
        })
    })
};

_Goods.prototype.Run = function(){
    var self = this;
    self.onClickEvent();
    self.edit();
    self.closeEventBTN();
    self.submitEditer();
    self.uploadImages()
};



$(function(){
    var goods = new _Goods();
    goods.Run();
});