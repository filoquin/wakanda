(window.webpackJsonp=window.webpackJsonp||[]).push([[9],{"9N29":function(o,e,i){"use strict";i.r(e),i.d(e,"routes",(function(){return p})),i.d(e,"UserModule",(function(){return a}));var t=i("ofXK"),r=i("3Pt+"),b=i("tyNb"),c=i("fXoL"),n=i("VITL");function l(o,e){if(1&o&&(c.Nb(0,"div",6),c.Nb(1,"div",7),c.Nb(2,"div",8),c.pc(3),c.Mb(),c.Mb(),c.Nb(4,"div",7),c.Nb(5,"div",8),c.pc(6),c.Mb(),c.Mb(),c.Nb(7,"div",7),c.Nb(8,"div",8),c.pc(9),c.Mb(),c.Mb(),c.Nb(10,"div",7),c.Nb(11,"div",8),c.pc(12),c.Mb(),c.Mb(),c.Nb(13,"div",7),c.Nb(14,"div",8),c.pc(15),c.Mb(),c.Mb(),c.Nb(16,"div",7),c.Nb(17,"div",8),c.pc(18),c.Mb(),c.Mb(),c.Nb(19,"div",7),c.Nb(20,"div",8),c.pc(21,"Productos m\xe1s vendido:"),c.Mb(),c.Mb(),c.Nb(22,"div",7),c.Nb(23,"div",8),c.pc(24),c.Mb(),c.Mb(),c.Nb(25,"div",0),c.Nb(26,"div",9),c.Nb(27,"a",10),c.pc(28,"Editar cuenta"),c.Mb(),c.Mb(),c.Mb(),c.Nb(29,"div",0),c.Nb(30,"div",9),c.Nb(31,"a",10),c.pc(32,"Cerrar sesion"),c.Mb(),c.Mb(),c.Mb(),c.Mb()),2&o){const o=c.Wb();c.xb(3),c.rc("Nombre y Apellido: ",o.profile.name,""),c.xb(3),c.rc("Mail: ",o.profile.email,""),c.xb(3),c.rc("Tel\xe9fono: ",o.profile.phone,""),c.xb(3),c.rc("Domicilio: ",o.profile.street,""),c.xb(3),c.rc("Productos Comprados: ",o.profile.product_uom_qty,""),c.xb(3),c.rc("Ganancia: ",o.profile.amount_total,""),c.xb(6),c.rc("Pedidos realizados: ",o.profile.order_count,"")}}let d=(()=>{class o{constructor(o){this.userService=o,this.profile={}}ngOnInit(){this.userService.getProfile().then(o=>{this.profile=o,console.log(o)}).catch(o=>{console.log(o)})}}return o.\u0275fac=function(e){return new(e||o)(c.Ib(n.a))},o.\u0275cmp=c.Cb({type:o,selectors:[["app-profile"]],decls:7,vars:1,consts:[[1,"row"],[1,"col-4"],[1,"col-4","text-center","mx-auto"],["src","assets/img/icons/profile-white.png",1,"img-fluid","p-4"],[1,"row","mt-4"],["class","col-10 profile-data p-2 mx-auto ",4,"ngIf"],[1,"col-10","profile-data","p-2","mx-auto"],[1,"row","text-profile","mt-2"],[1,"col-12"],[1,"col-12","text-center","mx-auto","mt-2"],["href","",1,"btn","btn-wkn"]],template:function(o,e){1&o&&(c.Nb(0,"div",0),c.Jb(1,"div",1),c.Nb(2,"div",2),c.Jb(3,"img",3),c.Mb(),c.Jb(4,"div",1),c.Mb(),c.Nb(5,"div",4),c.oc(6,l,33,7,"div",5),c.Mb()),2&o&&(c.xb(6),c.cc("ngIf",e.profile))},directives:[t.l],styles:[".profile-data[_ngcontent-%COMP%]{background-color:#fff;color:#fe2399;border-radius:10px}.text-profile[_ngcontent-%COMP%]{font-family:GlacialIndifference-Regular;font-size:.8em}"]}),o})();const p=[{path:"",component:d},{path:"profile",PathMatch:"full",component:d}];let a=(()=>{class o{}return o.\u0275mod=c.Gb({type:o}),o.\u0275inj=c.Fb({factory:function(e){return new(e||o)},imports:[[t.b,r.e,r.i,b.e.forChild(p)]]}),o})()}}]);