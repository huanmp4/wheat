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
    this.imagedown6 = $(".imagedown6");
    this.imagedown101 = $("#imagedown101");
    this.imagedown102 = $("#imagedown102");
    this.imagedown103 = $("#imagedown103");
    this.imagedown104 = $("#imagedown104");
}

//商业介绍图点击
_Goods.prototype.findEQ = function(){
    var self = this;
    var business_group = $(".business-group");
    console.log("1111");
    var group_count = business_group.children(".imagedown");
    if (group_count.length >= 5){
        xfzalert.alertError("不能再多了")
    }else{
        var imgName = "imagedown10" + group_count.length;
        var fileInputName = "imagedown20" + group_count.length;
        console.log("数量imgName",imgName);
        var tl = template("business-image",{"url":"http://127.0.0.1:8000/media/solid/bg_person.png","imgName":imgName,"fileInputName":fileInputName});
        business_group.prepend(tl);
        self.func2({"1":fileInputName,"2":imgName});
    }
};

//商业介绍图点击2
_Goods.prototype.func2 = function(e){
    var self = this;
    var _file = e["1"];
    var imgName = e["2"];
    var file = $("#" + _file);
    file.click();
    $("#"+imgName).on("click",function(){
        file.click();
    });
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
                    var img = $("#" + imgName);
                    img.attr("src",url);
                    img.attr("data-url",url);
                }else{
                    console.log("图片上传给服务器回调失败")
                }
            }
        })
    })
};

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
    self.imagedown6.click(function(e){
        e.preventDefault();
        self.findEQ()
    });
    self.imagedown101.click(function(e){
        e.preventDefault();
        self.func2({"1":"imagedown201","2":"imagedown101"})
    });
    self.imagedown102.click(function(e){
        e.preventDefault();
        console.log("222222222222222222222");
        self.func2({"1":"imagedown202","2":"imagedown102"})
    });
    self.imagedown103.click(function(e){
        e.preventDefault();
        self.func2({"1":"imagedown203","2":"imagedown103"})
    });
    self.imagedown104.click(function(e){
        e.preventDefault();
        self.func2({"1":"imagedown204","2":"imagedown104"})
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
        var shell = $(".shell-second");
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

        var businessImage = [];
        var file_p101 = $("#imagedown101").attr("data-url");
        var file_p102 = $("#imagedown102").attr("data-url");
        var file_p103 = $("#imagedown103").attr("data-url");
        var file_p104 = $("#imagedown104").attr("data-url");
        if (file_p101 && file_p101 !== ''){
            businessImage.push(file_p101)
        }
        if (file_p102 && file_p102 !== ''){
            businessImage.push(file_p102)
        }
        if (file_p103 && file_p103 !== ''){
            businessImage.push(file_p103)
        }
        if (file_p104 && file_p104 !== ''){
            businessImage.push(file_p104)
        }
        console.log("businessImage",businessImage);
        var businessImage1 = "["+businessImage.toString() + "]";
        console.log("businessImage:",businessImage);
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
                "standars":standars,
                "businessImage":businessImage1
            },
            "success":function(e){
                if (e.code ===200){
                    console.log("ok");
                    xfzalert.alertSuccess("修改成功")
                }
                else{
                    xfzalert.alertError("修改失败")
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
    self.uploadImages();
};



$(function(){
    var goods = new _Goods();
    goods.Run();
});