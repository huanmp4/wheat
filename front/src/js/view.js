function View(){
    this.closeBTN = $(".closeBTN");
    this.closeBTN1 = $(".closeBTN1");

    this.file0 = $(".file0");
    this.file1 = $(".file1");
    this.file2 = $(".file2");
    this.file3 = $(".file3");
    this.file4 = $(".file4");
    this.file5 = $(".file5");
    this.file6 = $(".file6");
    this.file7 = $(".file7");
    this.file8 = $(".file8");
    this.file9 = $(".file9");
    this.imagedown0 = $(".imagedown0");
    this.imagedown1 = $(".imagedown1");
    this.imagedown2 = $(".imagedown2");
    this.imagedown3 = $(".imagedown3");
    this.imagedown4 = $(".imagedown4");
    this.imagedown5 = $(".imagedown5");
    this.imagedown101 = $("#imagedown101");
    this.imagedown102 = $("#imagedown102");
    this.imagedown103 = $("#imagedown103");
    this.imagedown104 = $("#imagedown104");
}



View.prototype.uploadImages = function(){
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
    self.imagedown101.click(function(e){
        e.preventDefault();
        self.func({"1":self.file6,"2":self.imagedown101});
    });
    self.imagedown102.click(function(e){
        e.preventDefault();
        self.func({"1":self.file7,"2":self.imagedown102});
    });
    self.imagedown103.click(function(e){
        e.preventDefault();
        self.func({"1":self.file8,"2":self.imagedown103});
    });
    self.imagedown104.click(function(e){
        e.preventDefault();
        self.func({"1":self.file9,"2":self.imagedown104});
    });
};


View.prototype.func = function(e){
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



View.prototype.onClickEvent = function(){
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

View.prototype.closeEventBTN = function(){
    var self = this;
    self.closeBTN1.click(function(){
        $(".shell").css("visibility","hidden");
    })
};


View.prototype.edit = function(){
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
                    shell.find('.imagedown0').attr("data-url",data.detail);
                    shell.find('.imagedown5').attr("src",data.shoplogo);
                    shell.find('.imagedown5').attr("data-url",data.shoplogo);
                    shell.find('.imagedown1').attr("src",data.toppicture[0]);
                    shell.find('.imagedown1').attr("data-url",data.toppicture[0]);
                    shell.find('.imagedown2').attr("src",data.toppicture[1]);
                    shell.find('.imagedown2').attr("data-url",data.toppicture[1]);
                    shell.find('.imagedown3').attr("src",data.toppicture[2]);
                    shell.find('.imagedown3').attr("data-url",data.toppicture[2]);
                    shell.find('.imagedown4').attr("src",data.toppicture[3]);
                    shell.find('.imagedown4').attr("data-url",data.toppicture[3]);

                    var bsnArray = data.businessImage.replace("[",'').replace("]",'').split(",");
                    console.log("bsnArray",bsnArray);
                    if (bsnArray[0]){
                        shell.find('.imagedown101').attr("src",bsnArray[0]);
                        shell.find('.imagedown101').attr("data-url",bsnArray[0]);
                    }
                    if (bsnArray[1]){
                        shell.find('.imagedown102').attr("src",bsnArray[1]);
                        shell.find('.imagedown102').attr("data-url",bsnArray[1]);
                    }
                    if (bsnArray[2]){
                        shell.find('.imagedown103').attr("src",bsnArray[2]);
                        shell.find('.imagedown103').attr("data-url",bsnArray[2]);
                    }
                    if (bsnArray[3]){
                        shell.find('.imagedown104').attr("src",bsnArray[3]);
                        shell.find('.imagedown104').attr("data-url",bsnArray[3]);
                    }
                    shell.find('input[name="name"]').val(data.name);
                    shell.find('input[name="price"]').val(data.price);
                    shell.find('input[name="fare"]').val(data.fare);
                    shell.find('input[name="shopName"]').val(data.shop);

                    shell.find('input[name="standars"]').val(data.standars);
                    console.log("standars:",data.standars);
                    shell.find(".closeBTN1").attr("data-goodid",data.id)
                }
            }
        })
    })
};


View.prototype.submitEditer = function(){
    var self = this;
    var submit_edit = $(".btn-edit-confirm");
    submit_edit.click(function(){
        var shell = $(".shell");
        var good_id = shell.find('.closeBTN1').attr("data-goodid");
        var file_p0 = shell.find('.imagedown0').attr("data-url");
        var file_p1 = shell.find('.imagedown1').attr("data-url");
        var file_p2 = shell.find('.imagedown2').attr("data-url");
        var file_p3 = shell.find('.imagedown3').attr("data-url");
        var file_p4 = shell.find('.imagedown4').attr("data-url");
        var file_p5 = shell.find('.imagedown5').attr("data-url");
        console.log("file_p0",file_p0);
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
                "standars":standars,
                "businessImage":businessImage1
            },
            "success":function(e){
                if (e.code ===200){
                    console.log("ok");

                    xfzalert.alertSuccess("修改成功")
                }

            }
        })
    })
};

View.prototype.Run = function(){
    var self = this;
    self.onClickEvent();
    self.edit();
    self.closeEventBTN();
    self.submitEditer();
    self.uploadImages()
};



$(function(){
    var view = new View();
    view.Run();
});