(window.webpackJsonp=window.webpackJsonp||[]).push([[8],{DZYb:function(t,e,c){"use strict";c.r(e),c.d(e,"routes",(function(){return k})),c.d(e,"ProductsModule",(function(){return C}));var o=c("ofXK"),i=c("tyNb"),n=c("fXoL"),r=c("K3ix"),s=c("IKdg");function a(t,e){if(1&t){const t=n.Pb();n.Ob(0,"div",6),n.Ob(1,"a",7),n.Ob(2,"img",8),n.Vb("click",(function(){n.nc(t);const e=n.Zb();return e.removeProductQty(e.product)})),n.Nb(),n.Nb(),n.Nb()}}function l(t,e){if(1&t&&(n.Ob(0,"div",6),n.Ob(1,"strong"),n.wc(2),n.Nb(),n.Nb()),2&t){const t=n.Zb();n.xb(2),n.xc(t.product.qty_select?t.product.qty_select:0)}}function d(t,e){if(1&t){const t=n.Pb();n.Ob(0,"div",6),n.Ob(1,"a",7),n.Ob(2,"img",9),n.Vb("click",(function(){n.nc(t);const e=n.Zb();return e.addProductQty(e.product)})),n.Nb(),n.Nb(),n.Nb()}}function b(t,e){1&t&&(n.Ob(0,"div",10),n.Ob(1,"strong",11),n.wc(2,"AGOTADO"),n.Nb(),n.Nb())}let u=(()=>{class t{constructor(){}ngOnInit(){}removeProductQty(t){t.qty_select>0?t.qty_select-=1:alert("No puede realizar esta operacion")}addProductQty(t){t.qty_select||(t.qty_select=0),t.qty_select<t.immediately_usable_qty&&(t.qty_select+=1)}}return t.\u0275fac=function(e){return new(e||t)},t.\u0275cmp=n.Db({type:t,selectors:[["app-product-item"]],inputs:{product:"product"},decls:12,vars:8,consts:[[1,"row","item-product","m-2","p-1"],[1,"col-6","text-center","my-auto"],[1,"col-12"],[1,"col-12","text-center","my-auto"],["class","col-2 m-0 p-0 text-center my-auto",4,"ngIf"],["class","col-6 m-0 p-0 text-center my-auto",4,"ngIf"],[1,"col-2","m-0","p-0","text-center","my-auto"],[1,""],["src","assets/img/minus.png",1,"img-fluid",3,"click"],["src","assets/img/plus.png",1,"img-fluid",3,"click"],[1,"col-6","m-0","p-0","text-center","my-auto"],[1,"no-stock"]],template:function(t,e){1&t&&(n.Ob(0,"div",0),n.Ob(1,"div",1),n.Ob(2,"div",2),n.wc(3),n.Nb(),n.Ob(4,"div",3),n.Ob(5,"strong"),n.wc(6),n.ac(7,"currency"),n.Nb(),n.Nb(),n.Nb(),n.uc(8,a,3,0,"div",4),n.uc(9,l,3,1,"div",4),n.uc(10,d,3,0,"div",4),n.uc(11,b,3,0,"div",5),n.Nb()),2&t&&(n.xb(3),n.yc(" ",e.product.display_name," "),n.xb(3),n.xc(n.bc(7,6,e.product.user_price)),n.xb(2),n.gc("ngIf",e.product.immediately_usable_qty>0),n.xb(1),n.gc("ngIf",e.product.immediately_usable_qty>0),n.xb(1),n.gc("ngIf",e.product.immediately_usable_qty>0),n.xb(1),n.gc("ngIf",e.product.immediately_usable_qty<=0))},directives:[o.l],pipes:[o.c],styles:[".item-product[_ngcontent-%COMP%]{border-radius:5px;border:1px solid #fff;background-color:#fff;color:#ff5dbc;font-size:.8em}"]}),t})();function p(t,e){if(1&t&&(n.Ob(0,"div",5),n.Kb(1,"app-product-item",6),n.Nb()),2&t){const t=e.$implicit;n.xb(1),n.gc("product",t)}}let g=(()=>{class t{constructor(t,e){this.bsModalRef=t,this.saleOrderService=e,this.categoryName=null,this.event=new n.n,this.products=null}ngOnInit(){this.categoryName=this.category.name,this.saleOrderService.getProducts(this.category.id).then(t=>{var e=[];t.records.forEach((function(t,c,o){e.push(t),this.oldProductsSelected&&this.oldProductsSelected.forEach(e=>{t.id===e.id&&(t.qty_select=e.qty_select)})}),this),this.products=e}).catch(t=>{})}accept(){let t=[];this.products.forEach(e=>{e.qty_select&&t.push(e)}),this.event.emit({status:"OK",productsSelected:t}),this.bsModalRef.hide()}close(){this.bsModalRef.hide()}}return t.\u0275fac=function(e){return new(e||t)(n.Jb(r.a),n.Jb(s.a))},t.\u0275cmp=n.Db({type:t,selectors:[["app-product-select"]],decls:11,vars:2,consts:[[1,"row","p-2"],[1,"col-12","text-center"],["class","",4,"ngFor","ngForOf"],[1,"col-6","text-center"],[1,"btn","btn-sm","btn-wkn",3,"click"],[1,""],[3,"product"]],template:function(t,e){1&t&&(n.Ob(0,"div",0),n.Ob(1,"div",1),n.wc(2),n.Nb(),n.Nb(),n.uc(3,p,2,1,"div",2),n.Ob(4,"div",0),n.Ob(5,"div",3),n.Ob(6,"a",4),n.Vb("click",(function(){return e.close()})),n.wc(7,"Cerrar"),n.Nb(),n.Nb(),n.Ob(8,"div",3),n.Ob(9,"a",4),n.Vb("click",(function(){return e.accept()})),n.wc(10,"Aceptar"),n.Nb(),n.Nb(),n.Nb()),2&t&&(n.xb(2),n.yc(" ",e.categoryName," "),n.xb(1),n.gc("ngForOf",e.products))},directives:[o.k,u],styles:[""]}),t})();var m=c("5eHb"),h=c("IHAV"),f=c("4Lsd");const O=["textPopUpTemplate"];function x(t,e){if(1&t){const t=n.Pb();n.Ob(0,"div",19),n.Ob(1,"button",20),n.Vb("click",(function(){return n.nc(t),n.Zb().closeModal()})),n.Ob(2,"span",21),n.wc(3,"\xd7"),n.Nb(),n.Nb(),n.Nb(),n.Kb(4,"div",22)}if(2&t){const t=n.Zb();n.xb(4),n.gc("innerHTML",t.textPopUp,n.oc)}}function y(t,e){if(1&t){const t=n.Pb();n.Ob(0,"a",23),n.Vb("click",(function(){n.nc(t);const c=e.$implicit;return n.Zb().showProducts(c)})),n.Kb(1,"img",24),n.Ob(2,"div",25),n.wc(3),n.Nb(),n.Nb()}if(2&t){const t=e.$implicit;n.xb(1),n.ic("src","data:image/png;base64,",t.wkn_categ_image,"",n.qc),n.xb(2),n.yc(" ",t.name," ")}}let v=(()=>{class t{constructor(t,e,c,o,i,n,r){this.saleOrderService=t,this.bsModalService=e,this.router=c,this.platformLocation=o,this.toastrService=i,this.WakCatalogService=n,this.modalStatusService=r,this.categories=[],this.minHeight=20,this.rowMinHeight=20,this.total={quantity:0,amount:0,gain:0},this.productsSelected=[],localStorage.getItem("tmpOrder")&&(console.log("loading data..."),this.productsSelected=JSON.parse(localStorage.getItem("tmpOrder")),this.updateTotal()),o.onPopState(()=>this.bsModalService.hide(1))}onResize(t){this.computeHeigths()}ngOnInit(){this.computeHeigths(),this.saleOrderService.getCategories().then(t=>{this.categories=t.records,t.length<1&&this.router.navigate(["/login"]),this.modalStatusService.isNewsOpened()||(this.WakCatalogService.getPopUp().then(t=>{t&&t.length>0&&t[0].text&&(this.textPopUp=t[0].text,this.openModal())}),this.modalStatusService.setNewsOpened())}).catch(t=>{alert(t),this.router.navigate(["/login"]),console.log(t)})}showProducts(t){let e=null;this.productsSelected.forEach(c=>{c.category.id===t.id&&(e=c.productsSelected)}),this.bsModalRef=this.bsModalService.show(g,{initialState:{category:t,oldProductsSelected:e},class:"product-select"}),this.bsModalRef.content.event.subscribe(e=>{if("OK"===e.status){let c=!0;if(this.productsSelected.forEach(o=>{o.category.id===t.id&&(o.productsSelected=e.productsSelected,c=!1)}),c&&e.productsSelected.length>0){const c={category:null,productsSelected:null};c.category=t,c.productsSelected=e.productsSelected,this.productsSelected.push(c)}this.updateTotal()}})}next(){this.productsSelected.length>0?(localStorage.setItem("tmpOrder",JSON.stringify(this.productsSelected)),this.router.navigate(["/orders/summary"])):this.toastrService.warning("No selecciono ningun producto")}computeHeigths(){const t=window.outerHeight,e=(document.getElementById("title"),document.getElementById("summary").offsetHeight);this.minHeight=t-e-e-150,this.rowMinHeight=this.minHeight/3}updateTotal(){this.total.amount=0,this.total.gain=0,this.total.quantity=0,this.productsSelected.forEach(t=>{t.productsSelected.forEach(t=>{this.total.amount+=t.qty_select*t.user_price,this.total.gain+=t.qty_select*t.final_price-t.qty_select*t.user_price,this.total.quantity+=t.qty_select})})}clearOrder(){confirm("\xbfDesea vaciar la orden?")&&(this.productsSelected=[],this.total.amount=0,this.total.gain=0,this.total.quantity=0)}openModal(){this.bsModalRef=this.bsModalService.show(this.textPopUpTemplate,{class:"modal-lg"})}closeModal(){this.bsModalRef.hide()}}return t.\u0275fac=function(e){return new(e||t)(n.Jb(s.a),n.Jb(r.b),n.Jb(i.c),n.Jb(o.o),n.Jb(m.b),n.Jb(h.a),n.Jb(f.a))},t.\u0275cmp=n.Db({type:t,selectors:[["app-product-list"]],viewQuery:function(t,e){var c;1&t&&n.Ac(O,!0),2&t&&n.kc(c=n.Wb())&&(e.textPopUpTemplate=c.first)},hostBindings:function(t,e){1&t&&n.Vb("resize",(function(t){return e.onResize(t)}),!1,n.mc)},decls:34,vars:8,consts:[["textPopUpTemplate",""],[1,"fill","container-main"],[1,"container","pt-1","text-center"],["id","title",1,"row","pt-3","pb-1"],[1,"col-12","text-center"],[1,"product-title","m-2","text-uppercase","text-white"],[1,"container-products"],[1,"container-category"],[3,"click",4,"ngFor","ngForOf"],["id","summary",1,"summary","mr-1","ml-1"],[1,"mt-2","pt-0","pb-0","pl-4","pr-4","text-left","mb-0"],[1,""],[1,"container-resume","mt-2","pt-0","pb-1","pl-4","pr-4"],[1,"text-resume","text-left"],[1,"mb-0"],[1,"buttons-resume"],[1,"text-right"],[1,"btn","btn-sm","btn-wkn2","text-uppercase",3,"click"],[1,"btn","btn-sm","btn-wkn","text-uppercase",3,"click"],[1,"modal-header"],["type","button",1,"close",3,"click"],["aria-hidden","true"],[1,"modal-body",3,"innerHTML"],[3,"click"],[1,"img-circle","p-2",3,"src"],[1,"text-category","text-center","mx-auto","text-uppercase"]],template:function(t,e){1&t&&(n.uc(0,x,5,1,"ng-template",null,0,n.vc),n.Ob(2,"div",1),n.Ob(3,"div",2),n.Ob(4,"div",3),n.Ob(5,"div",4),n.Ob(6,"h5",5),n.wc(7,"Categorias"),n.Nb(),n.Nb(),n.Nb(),n.Ob(8,"div",6),n.Ob(9,"div",7),n.uc(10,y,4,2,"a",8),n.Nb(),n.Ob(11,"div",9),n.Ob(12,"div",10),n.Ob(13,"h6",11),n.Ob(14,"u"),n.wc(15,"Resumen del pedido"),n.Nb(),n.Nb(),n.Nb(),n.Ob(16,"div",12),n.Ob(17,"div",13),n.Ob(18,"span",14),n.wc(19),n.Nb(),n.Ob(20,"div",11),n.Ob(21,"span",14),n.wc(22),n.ac(23,"currency"),n.Nb(),n.Nb(),n.Ob(24,"div",11),n.Ob(25,"span",14),n.wc(26),n.ac(27,"currency"),n.Nb(),n.Nb(),n.Nb(),n.Ob(28,"div",15),n.Ob(29,"div",16),n.Ob(30,"a",17),n.Vb("click",(function(){return e.clearOrder()})),n.wc(31,"Vaciar"),n.Nb(),n.Ob(32,"a",18),n.Vb("click",(function(){return e.next()})),n.wc(33,"siguiente"),n.Nb(),n.Nb(),n.Nb(),n.Nb(),n.Nb(),n.Nb(),n.Nb(),n.Nb()),2&t&&(n.xb(10),n.gc("ngForOf",e.categories),n.xb(9),n.yc("Productos comprados: ",e.total.quantity,""),n.xb(3),n.yc("Total: ",n.bc(23,4,e.total.amount),""),n.xb(4),n.yc(" Ganancia: ",n.bc(27,6,e.total.gain),""))},directives:[o.k],pipes:[o.c],styles:[".container-main[_ngcontent-%COMP%]{background-color:#ffd3f2!important}.container-category[_ngcontent-%COMP%]{display:grid;grid-template-columns:repeat(2,1fr);height:calc(100vh - 300px);overflow-y:scroll;padding-bottom:30px;position:relative}[_ngcontent-%COMP%]::-webkit-scrollbar{width:12px;height:8px}[_ngcontent-%COMP%]::-webkit-scrollbar-thumb{border-radius:10px;background-color:#ff5dbc}[_ngcontent-%COMP%]::-webkit-scrollbar-track{background-color:#eee;border-radius:10px}.btn-product[_ngcontent-%COMP%]{background-color:#ff5dbc;color:#fff}.down-arrow[_ngcontent-%COMP%]{position:-webkit-sticky;position:sticky;bottom:0;left:100vw;height:20px;width:20px;background-color:#fff;color:pink;border-radius:15px}.product-title[_ngcontent-%COMP%]{background-color:#ff5dbc;font-family:AronGrotesque-Regular;font-size:1.5em;border-radius:5px}.container-products[_ngcontent-%COMP%]{display:flex;flex-direction:column}.summary[_ngcontent-%COMP%]{background-color:#ffbce4;border-radius:15px;margin-bottom:60px;color:#fff;position:fixed;bottom:0;left:0;right:0;font-size:.8em}.text-category[_ngcontent-%COMP%]{color:#ff5dbc;font-size:.8em;font-family:GlacialIndifference-Regular;font-weight:bolder}.img-circle[_ngcontent-%COMP%]{margin-top:5%;background-color:#fff;border-radius:50%;width:80px;height:80px}@media (min-width:280px){.container-category[_ngcontent-%COMP%]{grid-template-columns:repeat(3,1fr)}}@media (min-height:820px){.img-circle[_ngcontent-%COMP%]{background-color:#fff;border-radius:50%;width:95px;height:95px}}@media (min-width:428px){.img-circle[_ngcontent-%COMP%]{width:140px;height:140px}.product-title[_ngcontent-%COMP%]{font-size:1.5em}}@media (min-width:576px){.img-circle[_ngcontent-%COMP%]{width:150px;height:150px}.product-title[_ngcontent-%COMP%]{font-size:2em}}@media (min-width:768px){.img-circle[_ngcontent-%COMP%]{width:175px;height:175px}.product-title[_ngcontent-%COMP%]{font-size:2em}}@media (min-width:992px){.img-circle[_ngcontent-%COMP%]{width:180px;height:180px}.product-title[_ngcontent-%COMP%]{font-size:2.5em}}@media (min-width:1200px){.img-circle[_ngcontent-%COMP%]{width:180px;height:180px}.product-title[_ngcontent-%COMP%]{font-size:2.5em}}@media (max-height:600px){.img-circle[_ngcontent-%COMP%]{width:55px;height:55px}}.container-resume[_ngcontent-%COMP%]{display:flex;flex-direction:start}.buttons-resume[_ngcontent-%COMP%]{display:flex;width:50%;justify-content:flex-end;flex-direction:column}.text-resume[_ngcontent-%COMP%]{width:50%}.modal-header[_ngcontent-%COMP%]{position:relative}.modal-title[_ngcontent-%COMP%]{position:absolute;top:10px;left:10px}"]}),t})();function w(t,e){if(1&t&&(n.Ob(0,"li"),n.wc(1),n.Nb()),2&t){const t=e.$implicit;n.xb(1),n.yc(" ",t.name," ")}}function N(t,e){if(1&t&&(n.Ob(0,"div",11),n.Ob(1,"div",12),n.Ob(2,"h4",13),n.Ob(3,"u"),n.wc(4),n.Nb(),n.Nb(),n.Nb(),n.Ob(5,"div",14),n.Ob(6,"ul"),n.uc(7,w,2,1,"li",15),n.Nb(),n.Nb(),n.Nb()),2&t){const t=e.$implicit;n.xb(4),n.yc(" ",t.category," "),n.xb(3),n.gc("ngForOf",t.products)}}function _(t,e){if(1&t&&(n.Ob(0,"div",4),n.Ob(1,"div",5),n.Ob(2,"div",6),n.Kb(3,"img",7),n.Nb(),n.Ob(4,"div",8),n.Ob(5,"div",9),n.wc(6,"Productos "),n.Kb(7,"br"),n.wc(8," m\xe1s "),n.Kb(9,"br"),n.wc(10," vendidos"),n.Nb(),n.Nb(),n.Nb(),n.uc(11,N,8,2,"div",10),n.Nb()),2&t){const t=n.Zb();n.xb(11),n.gc("ngForOf",t.bestsellers)}}let P=(()=>{class t{constructor(t){this.saleOrderService=t,this.bestsellers=[],this.lastCategoryName=""}ngOnInit(){this.saleOrderService.getSaleRank().then(t=>{console.log(t.records),this.sortAndFillByCategory(t.records)}).catch(t=>{console.log(t)})}sortAndFillByCategory(t){const e=[];t.forEach(t=>{e.find(e=>e===t.category_name)||e.push(t.category_name)}),console.log(e),e.forEach(e=>{let c={category:e,products:[]};t.forEach(t=>{c.category=e,e===t.category_name&&c.products.push(t)}),this.bestsellers.push(c)}),console.log(this.bestsellers)}}return t.\u0275fac=function(e){return new(e||t)(n.Jb(s.a))},t.\u0275cmp=n.Db({type:t,selectors:[["app-product-betsellers"]],decls:4,vars:1,consts:[[1,"fill","container-main"],[1,"container","pt-1","pb-2","text-center","edit"],[1,"row","bestsellers-main","mt-2","ml-1","mr-1","custom-mb"],["class","col-md-12 col-12 mx-auto",4,"ngIf"],[1,"col-md-12","col-12","mx-auto"],[1,"row","mt-2","justify-content-end","mb-2"],[1,"col-4","my-auto","d-flex"],["src","assets/img/logo-white.png",1,"img-fluid","mr-2","logo","align-self-start","my-auto"],[1,"col-7","text-center","my-auto"],[1,"order","m-2","text-white","p-2","text-big","text-uppercase"],["class","row text-white",4,"ngFor","ngForOf"],[1,"row","text-white"],[1,"col-12","ml-4","text-left"],[1,"text-uppercase"],[1,"col-12","text-left"],[4,"ngFor","ngForOf"]],template:function(t,e){1&t&&(n.Ob(0,"div",0),n.Ob(1,"div",1),n.Ob(2,"div",2),n.uc(3,_,12,1,"div",3),n.Nb(),n.Nb(),n.Nb()),2&t&&(n.xb(3),n.gc("ngIf",e.bestsellers))},directives:[o.l,o.k],styles:[".logo[_ngcontent-%COMP%]{width:2.5em}.text-logo[_ngcontent-%COMP%]{font-family:AronGrotesque-Regular;font-size:2.25em;display:inline-block}.container-main[_ngcontent-%COMP%]{background-color:#ffd3f2!important;margin-bottom:60px}.bestsellers-main[_ngcontent-%COMP%]{background-color:#ff5dbc;border-radius:15px}.text-price[_ngcontent-%COMP%]{font-size:.8em}.text-small[_ngcontent-%COMP%]{font-size:x-small}.logo[_ngcontent-%COMP%]{width:5.5em;vertical-align:center;display:inline-block}.custom-mb[_ngcontent-%COMP%]{margin-bottom:65px}.text-uppercase[_ngcontent-%COMP%]{text-transform:uppercase;font-weight:700;font-size:1.2em}"]}),t})();var M=c("p3Fh");const k=[{path:"",component:v,canActivate:[M.a]},{path:"bestsellers",component:P,canActivate:[M.a]}];let C=(()=>{class t{}return t.\u0275mod=n.Hb({type:t}),t.\u0275inj=n.Gb({factory:function(e){return new(e||t)},providers:[r.b],imports:[[o.b,i.e.forChild(k),r.c.forRoot()]]}),t})()}}]);