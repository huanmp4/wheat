function Home(){
    this.uploadIMG = $("uploadIMG");
    this.submitBTN = $("#submitBTN");
    this.formTable = $(".formTables");
    this.businessgroup = $(".business-group");
    this.file0 = $(".file0");
    this.file1 = $(".file1");
    this.file2 = $(".file2");
    this.file3 = $(".file3");
    this.file4 = $(".file4");
    this.file5 = $(".file5");
    this.file6 = $(".file6");
    this.file10 = $(".file10");
    this.imagedown0 = $(".imagedown0");
    this.imagedown1 = $(".imagedown1");
    this.imagedown2 = $(".imagedown2");
    this.imagedown3 = $(".imagedown3");
    this.imagedown4 = $(".imagedown4");
    this.imagedown5 = $(".imagedown5");
    this.imagedown6 = $(".imagedown6");
}


//商业介绍图点击
Home.prototype.findEQ = function(){
    var self = this;
    var business_group = $(".business-group");
    var group_count = business_group.children(".imagedown");
    if (group_count.length >= 5){
        xfzalert.alertError("不能再多了")
    }else{
        var imgName = "imagedown10" + group_count.length;
        var fileInputName = "imagedown20" + group_count.length;
        var tl = template("business-image",{"url":"http://127.0.0.1:8000/media/solid/bg_person.png","imgName":imgName,"fileInputName":fileInputName});
        business_group.append(tl);
        var file = $("#" + fileInputName);
        self.func2({"1":file,"2":imgName});
    }
};

//商业介绍图点击2
Home.prototype.func2 = function(e){

    var self = this;
    var file = e["1"];
    var imgName = e["2"];
    file.click();
    console.log("22222222222",file);
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

Home.prototype.onclick = function(){
    var inputGroupFile01 = $("#inputGroupFile01");
    var self = this;
    inputGroupFile01.change(function(){
        var file = this.files[0];
        var formdata = new FormData();
        formdata.append("file",file);
        console.log("file:",file);
        xfzajax.post({
            "url":"/imageupdata",
            "data":formdata,
            "processData":false,
            "contentType":false,
            "success":function(e){
                console.log("e",e)
            }
        })
    });
};

Home.prototype.uploadImages = function(){
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
};


Home.prototype.func = function(e){
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


Home.prototype.submitFormEvent = function(){
    var self = this;
    self.submitBTN.click(function(e){
        e.preventDefault();
        var file_p0 = self.imagedown0.attr("data-url");
        var file_p1 = self.imagedown1.attr("data-url");
        var file_p2 = self.imagedown2.attr("data-url");
        var file_p3 = self.imagedown3.attr("data-url");
        var file_p4 = self.imagedown4.attr("data-url");
        var file_p5 = self.imagedown5.attr("data-url");
        var name = self.formTable.find("input[name='name']").val();
        var price = self.formTable.find("input[name='price']").val();
        var fare = self.formTable.find("input[name='fare']").val();
        var shop = self.formTable.find("input[name='shopName']").val();
        var standars = self.formTable.find("input[name='standars']").val();

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

        xfzajax.post({
            "url":"/writeIndatabase",
            "data":{
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
                if(e.code === 200){
                    xfzalert.alertSuccess("商品已添加成功");
                    console.log("商品已添加成功,保留缓存数据")
                }
            }
        })
    })
};

Home.prototype.Run = function(){
    var self = this;
    self.onclick();
    self.uploadImages();
    self.submitFormEvent();
};

$(function(){
    var home = new Home();
    home.Run();
});