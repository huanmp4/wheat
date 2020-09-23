function Home(){
    this.uploadIMG = $("uploadIMG");
    this.submitBTN = $("#submitBTN");
    this.formTable = $(".formTables");
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
                "standars":standars
            },
            "success":function(e){
                if(e.code === 200){
                    console.log("成功添加")
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