(window.webpackJsonp=window.webpackJsonp||[]).push([[6],{fAJX:function(e,t,r){"use strict";r.r(t),r.d(t,"routes",(function(){return f})),r.d(t,"OrdersModule",(function(){return K}));var o=r("ofXK"),c=r("fXoL");let i=(()=>{class e{constructor(){}ngOnInit(){}}return e.\u0275fac=function(t){return new(t||e)},e.\u0275cmp=c.Cb({type:e,selectors:[["app-order-list"]],decls:5,vars:0,consts:[[1,"container","h-100"],[1,"row","h-100","justify-content-center","align-items-center"],[1,"col-12","text-center"]],template:function(e,t){1&e&&(c.Lb(0,"div",0),c.Lb(1,"div",1),c.Lb(2,"div",2),c.Lb(3,"h6"),c.kc(4,"Pedidos en desarrollo...."),c.Kb(),c.Kb(),c.Kb(),c.Kb())},styles:[""]}),e})();var s=r("tyNb"),n=r("IKdg");function b(e,t){if(1&e&&(c.Lb(0,"div",1),c.Lb(1,"div",5),c.kc(2),c.Kb(),c.Lb(3,"div",13),c.kc(4),c.Kb(),c.Lb(5,"div",14),c.kc(6),c.Vb(7,"currency"),c.Kb(),c.Kb()),2&e){const e=t.$implicit;c.xb(2),c.mc(" -",e.name," "),c.xb(2),c.mc(" ",e.qty_select," "),c.xb(2),c.mc(" ",c.Wb(7,3,e.user_price)," ")}}function d(e,t){if(1&e&&(c.Lb(0,"div",11),c.jc(1,b,8,5,"div",16),c.Kb()),2&e){const e=t.$implicit;c.xb(1),c.Zb("ngForOf",e.productsSelected)}}function a(e,t){if(1&e&&(c.Lb(0,"div",11),c.Lb(1,"div",1),c.Lb(2,"div",12),c.kc(3," Producto "),c.Kb(),c.Lb(4,"div",13),c.kc(5," Cantidad "),c.Kb(),c.Lb(6,"div",14),c.kc(7," Precio "),c.Kb(),c.Kb(),c.jc(8,d,2,1,"div",15),c.Kb()),2&e){const e=c.Ub();c.xb(8),c.Zb("ngForOf",e.order)}}function l(e,t){if(1&e){const e=c.Mb();c.Lb(0,"div",1),c.Lb(1,"div",5),c.kc(2),c.Kb(),c.Lb(3,"div",9),c.kc(4),c.Kb(),c.Lb(5,"div",10),c.Lb(6,"div",12),c.Lb(7,"a",7),c.Lb(8,"img",13),c.Sb("click",(function(){c.fc(e);const r=t.$implicit;return c.Ub(2).selectPromo(r.id)})),c.Kb(),c.Kb(),c.Kb(),c.Kb(),c.Kb()}if(2&e){const e=t.$implicit;c.xb(2),c.mc(" -",e.product_id[1]," "),c.xb(2),c.mc(" ",e.product_qty," ")}}function v(e,t){if(1&e&&(c.Lb(0,"div",7),c.Lb(1,"div",1),c.Lb(2,"div",8),c.kc(3," Producto "),c.Kb(),c.Lb(4,"div",9),c.kc(5," Cantidad "),c.Kb(),c.Jb(6,"div",10),c.Kb(),c.Lb(7,"div",7),c.jc(8,l,9,2,"div",11),c.Kb(),c.Kb()),2&e){const e=c.Ub();c.xb(8),c.Zb("ngForOf",e.promos)}}function u(e,t){if(1&e){const e=c.Mb();c.Lb(0,"div",1),c.Lb(1,"div",5),c.kc(2),c.Kb(),c.Lb(3,"div",9),c.kc(4),c.Kb(),c.Lb(5,"div",10),c.Lb(6,"div",12),c.Lb(7,"a",13),c.Sb("click",(function(){c.fc(e);const r=t.$implicit;return c.Ub(2).selectCarrier(r)})),c.kc(8,"elegir "),c.Kb(),c.Kb(),c.Kb(),c.Kb()}if(2&e){const e=t.$implicit;c.xb(2),c.mc(" -",e.display_name," "),c.xb(2),c.mc(" ",e.amount," ")}}function m(e,t){if(1&e&&(c.Lb(0,"div",7),c.Lb(1,"div",1),c.Lb(2,"div",8),c.kc(3," Envio "),c.Kb(),c.Lb(4,"div",9),c.kc(5," Precio "),c.Kb(),c.Jb(6,"div",10),c.Kb(),c.Lb(7,"div",7),c.jc(8,u,9,2,"div",11),c.Kb(),c.Kb()),2&e){const e=c.Ub();c.xb(8),c.Zb("ngForOf",e.carriers)}}function p(e,t){if(1&e&&(c.Lb(0,"tr"),c.Lb(1,"td"),c.kc(2),c.Kb(),c.Lb(3,"td"),c.kc(4),c.Kb(),c.Lb(5,"td"),c.kc(6),c.Kb(),c.Kb()),2&e){const e=t.$implicit;c.xb(2),c.mc("",e.product_uom_qty," "),c.xb(2),c.lc(e.name),c.xb(2),c.lc(e.price_total)}}function h(e,t){if(1&e&&(c.Lb(0,"div",2),c.Lb(1,"table",8),c.Lb(2,"tr"),c.Lb(3,"th"),c.kc(4,"C"),c.Kb(),c.Lb(5,"th"),c.kc(6,"Descripcion"),c.Kb(),c.Lb(7,"th"),c.kc(8,"Total"),c.Kb(),c.Kb(),c.jc(9,p,7,3,"tr",9),c.Kb(),c.Kb()),2&e){const e=c.Ub(2);c.xb(9),c.Zb("ngForOf",e.orderLines)}}function L(e,t){if(1&e&&(c.Lb(0,"div",1),c.Lb(1,"div",2),c.Lb(2,"div",3),c.Lb(3,"h2",4),c.kc(4),c.Kb(),c.Kb(),c.Kb(),c.Lb(5,"div",2),c.Lb(6,"div",3),c.Lb(7,"p",4),c.kc(8),c.Kb(),c.Kb(),c.Kb(),c.Lb(9,"div",2),c.Lb(10,"div",5),c.kc(11),c.Kb(),c.Lb(12,"div",5),c.kc(13," Total "),c.Kb(),c.Kb(),c.jc(14,h,10,1,"div",6),c.Jb(15,"div",7),c.Kb()),2&e){const e=c.Ub();c.xb(4),c.mc("Pedido ",e.order.display_name," recibido"),c.xb(4),c.mc("Hemos recibido el pedido ",e.order.display_name,". Utilice ese numero para posteriores referencias."),c.xb(3),c.mc(" Fecha: ",e.order.date_order," "),c.xb(3),c.Zb("ngIf",e.orderLines)}}const f=[{path:"",component:i},{path:"summary",component:(()=>{class e{constructor(e,t){this.saleOrderService=e,this.router=t,this.order=null,this.total=0,this.lines=[],this.order=JSON.parse(localStorage.getItem("tmpOrder")),this.order.forEach(e=>{e.productsSelected.forEach(e=>{this.lines.push({id:e.id,qty:e.qty_select}),this.total+=e.qty_select*e.user_price})})}ngOnInit(){}saveOrder(){this.saleOrderService.createSaleOrder(this.lines).then(e=>{if(console.log(e),e){let t=e[0].id;this.router.navigate(e[0].show_promos?["/orders/promos/"+t]:["/orders/delivery/"+t]),localStorage.removeItem("tmpOrder")}}).catch(e=>{console.log(e)})}}return e.\u0275fac=function(t){return new(t||e)(c.Ib(n.a),c.Ib(s.c))},e.\u0275cmp=c.Cb({type:e,selectors:[["app-order-sumary"]],decls:19,vars:4,consts:[[1,"container","mt-2"],[1,"row"],["cass","col-12"],[1,"mb-0"],["class","",4,"ngIf"],[1,"col-6"],[1,"col-6","text-right"],[1,"row","order-actions","mx-auto","w-100"],[1,"col-6","text-left"],["routerLink","",1,"btn","btn-wkn","btn-sm","text-uppercase","pull-left"],[1,"btn","btn-wkn","btn-sm","text-uppercase","pull-right",3,"click"],[1,""],[1,"col-6","text-center"],[1,"col-2","text-center"],[1,"col-4","text-center"],["class","",4,"ngFor","ngForOf"],["class","row",4,"ngFor","ngForOf"]],template:function(e,t){1&e&&(c.Lb(0,"div",0),c.Lb(1,"div",1),c.Lb(2,"div",2),c.Lb(3,"h6",3),c.Lb(4,"u"),c.kc(5,"Resumen del pedido"),c.Kb(),c.Kb(),c.Kb(),c.Kb(),c.jc(6,a,9,1,"div",4),c.Kb(),c.Lb(7,"div",1),c.Jb(8,"div",5),c.Lb(9,"div",6),c.kc(10),c.Vb(11,"currency"),c.Kb(),c.Kb(),c.Lb(12,"div",7),c.Lb(13,"div",8),c.Lb(14,"a",9),c.kc(15," volver"),c.Kb(),c.Kb(),c.Lb(16,"div",6),c.Lb(17,"a",10),c.Sb("click",(function(){return t.saveOrder()})),c.kc(18," finalizar"),c.Kb(),c.Kb(),c.Kb()),2&e&&(c.xb(6),c.Zb("ngIf",t.order),c.xb(4),c.mc(" Total : ",c.Wb(11,2,t.total)," "))},directives:[o.k,s.d,o.j],pipes:[o.c],styles:[".order-actions[_ngcontent-%COMP%]{position:fixed;bottom:65px}"]}),e})()},{path:"promos/:id",component:(()=>{class e{constructor(e,t,r){this.actRoute=e,this.saleOrderService=t,this.router=r,this.promos=[]}ngOnInit(){this.orderId=Number(this.actRoute.snapshot.paramMap.get("id")),this.loadPromos(this.orderId)}loadPromos(e){this.saleOrderService.getPromos(e).then(e=>{0==e.length&&this.router.navigate(["/orders/delivery/"+this.orderId]),this.promos=e}).catch(e=>{console.log("errors"+e)})}selectPromo(e){this.saleOrderService.selectPromo(e).then(e=>{0==e.length&&this.router.navigate(["/orders/delivery/"+this.orderId]),this.promos=e,console.log(this.promos)}).catch(e=>{console.log("errors"+e)})}}return e.\u0275fac=function(t){return new(t||e)(c.Ib(s.a),c.Ib(n.a),c.Ib(s.c))},e.\u0275cmp=c.Cb({type:e,selectors:[["app-order-promos"]],decls:10,vars:1,consts:[[1,"container","mt-2"],[1,"row"],["cass","col-12"],[1,"mb-0"],["class","",4,"ngIf"],[1,"col-6"],[1,"row","order-actions","mx-auto","w-100"],[1,""],[1,"col-6","text-center"],[1,"col-2","text-center"],[1,"col-4","text-center"],["class","row",4,"ngFor","ngForOf"],[1,"col-1","m-0","p-0","text-center","my-auto"],["src","assets/img/plus.png",1,"img-fluid",3,"click"]],template:function(e,t){1&e&&(c.Lb(0,"div",0),c.Lb(1,"div",1),c.Lb(2,"div",2),c.Lb(3,"h6",3),c.Lb(4,"u"),c.kc(5,"Promociones"),c.Kb(),c.Kb(),c.Kb(),c.Kb(),c.jc(6,v,9,1,"div",4),c.Kb(),c.Lb(7,"div",1),c.Jb(8,"div",5),c.Kb(),c.Jb(9,"div",6)),2&e&&(c.xb(6),c.Zb("ngIf",t.promos))},directives:[o.k,o.j],styles:[""]}),e})()},{path:"delivery/:id",component:(()=>{class e{constructor(e,t,r){this.actRoute=e,this.saleOrderService=t,this.router=r,this.carriers=[]}ngOnInit(){this.orderId=Number(this.actRoute.snapshot.paramMap.get("id")),this.getCarriers(this.orderId)}getCarriers(e){this.saleOrderService.getCarriers(e).then(e=>{console.log(e),this.carriers=e}).catch(e=>{console.log("errors"+e)})}selectCarrier(e){this.saleOrderService.deliveryConfirm(this.orderId,e.id,e.amount).then(e=>{this.router.navigate(["/orders/confirm/"+this.orderId])}).catch(e=>{console.log("errors"+e)})}}return e.\u0275fac=function(t){return new(t||e)(c.Ib(s.a),c.Ib(n.a),c.Ib(s.c))},e.\u0275cmp=c.Cb({type:e,selectors:[["app-order-delivery"]],decls:10,vars:1,consts:[[1,"container","mt-2"],[1,"row"],["cass","col-12"],[1,"mb-0"],["class","",4,"ngIf"],[1,"col-6"],[1,"row","order-actions","mx-auto","w-100"],[1,""],[1,"col-6","text-center"],[1,"col-2","text-center"],[1,"col-4","text-center"],["class","row",4,"ngFor","ngForOf"],[1,"col-1","m-0","p-0","text-center","my-auto"],[1,"",3,"click"]],template:function(e,t){1&e&&(c.Lb(0,"div",0),c.Lb(1,"div",1),c.Lb(2,"div",2),c.Lb(3,"h6",3),c.Lb(4,"u"),c.kc(5,"Envio"),c.Kb(),c.Kb(),c.Kb(),c.Kb(),c.jc(6,m,9,1,"div",4),c.Kb(),c.Lb(7,"div",1),c.Jb(8,"div",5),c.Kb(),c.Jb(9,"div",6)),2&e&&(c.xb(6),c.Zb("ngIf",t.carriers))},directives:[o.k,o.j],styles:[""]}),e})()},{path:"confirm/:id",component:(()=>{class e{constructor(e,t,r){this.actRoute=e,this.saleOrderService=t,this.router=r}ngOnInit(){this.orderId=Number(this.actRoute.snapshot.paramMap.get("id")),this.getOrder(this.orderId)}getOrder(e){this.saleOrderService.getOrder(e).then(e=>{this.order=e[0]}).catch(e=>{console.log("errors"+e)}),this.saleOrderService.getOrderLines(e).then(e=>{this.orderLines=e.records}).catch(e=>{console.log("errors"+e)})}}return e.\u0275fac=function(t){return new(t||e)(c.Ib(s.a),c.Ib(n.a),c.Ib(s.c))},e.\u0275cmp=c.Cb({type:e,selectors:[["app-order-confirm"]],decls:1,vars:1,consts:[["class","container mt-2",4,"ngIf"],[1,"container","mt-2"],[1,"row"],["cass","col-12"],[1,"mb-0"],[1,"col-6"],["class","row",4,"ngIf"],[1,"row","order-actions","mx-auto","w-100"],[1,"table"],[4,"ngFor","ngForOf"]],template:function(e,t){1&e&&c.jc(0,L,16,4,"div",0),2&e&&c.Zb("ngIf",t.order)},directives:[o.k,o.j],styles:[""]}),e})()}];let K=(()=>{class e{}return e.\u0275mod=c.Gb({type:e}),e.\u0275inj=c.Fb({factory:function(t){return new(t||e)},imports:[[o.b,s.e.forChild(f)]]}),e})()}}]);