(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-6d072ae6"],{"0cb2":function(e,t,r){var n=r("7b0b"),o=Math.floor,a="".replace,i=/\$([$&'`]|\d{1,2}|<[^>]*>)/g,l=/\$([$&'`]|\d{1,2})/g;e.exports=function(e,t,r,c,s,u){var m=r+e.length,p=c.length,d=l;return void 0!==s&&(s=n(s),d=i),a.call(u,d,(function(n,a){var i;switch(a.charAt(0)){case"$":return"$";case"&":return e;case"`":return t.slice(0,r);case"'":return t.slice(m);case"<":i=s[a.slice(1,-1)];break;default:var l=+a;if(0===l)return n;if(l>p){var u=o(l/10);return 0===u?n:u<=p?void 0===c[u-1]?a.charAt(1):c[u-1]+a.charAt(1):n}i=c[l-1]}return void 0===i?"":i}))}},"14c3":function(e,t,r){var n=r("c6b6"),o=r("9263");e.exports=function(e,t){var r=e.exec;if("function"===typeof r){var a=r.call(e,t);if("object"!==typeof a)throw TypeError("RegExp exec method returned something other than an Object or null");return a}if("RegExp"!==n(e))throw TypeError("RegExp#exec called on incompatible receiver");return o.call(e,t)}},"25f0":function(e,t,r){"use strict";var n=r("6eeb"),o=r("825a"),a=r("d039"),i=r("ad6d"),l="toString",c=RegExp.prototype,s=c[l],u=a((function(){return"/a/b"!=s.call({source:"a",flags:"b"})})),m=s.name!=l;(u||m)&&n(RegExp.prototype,l,(function(){var e=o(this),t=String(e.source),r=e.flags,n=String(void 0===r&&e instanceof RegExp&&!("flags"in c)?i.call(e):r);return"/"+t+"/"+n}),{unsafe:!0})},"44e7":function(e,t,r){var n=r("861d"),o=r("c6b6"),a=r("b622"),i=a("match");e.exports=function(e){var t;return n(e)&&(void 0!==(t=e[i])?!!t:"RegExp"==o(e))}},"4d63":function(e,t,r){var n=r("83ab"),o=r("da84"),a=r("94ca"),i=r("7156"),l=r("9bf2").f,c=r("241c").f,s=r("44e7"),u=r("ad6d"),m=r("9f7f"),p=r("6eeb"),d=r("d039"),f=r("69f3").set,v=r("2626"),x=r("b622"),g=x("match"),b=o.RegExp,h=b.prototype,_=/a/g,F=/a/g,S=new b(_)!==_,y=m.UNSUPPORTED_Y,E=n&&a("RegExp",!S||y||d((function(){return F[g]=!1,b(_)!=_||b(F)==F||"/a/i"!=b(_,"i")})));if(E){var R=function(e,t){var r,n=this instanceof R,o=s(e),a=void 0===t;if(!n&&o&&e.constructor===R&&a)return e;S?o&&!a&&(e=e.source):e instanceof R&&(a&&(t=u.call(e)),e=e.source),y&&(r=!!t&&t.indexOf("y")>-1,r&&(t=t.replace(/y/g,"")));var l=i(S?new b(e,t):b(e,t),n?this:h,R);return y&&r&&f(l,{sticky:r}),l},k=function(e){e in R||l(R,e,{configurable:!0,get:function(){return b[e]},set:function(t){b[e]=t}})},$=c(b),w=0;while($.length>w)k($[w++]);h.constructor=R,R.prototype=h,p(o,"RegExp",R)}v("RegExp")},5319:function(e,t,r){"use strict";var n=r("d784"),o=r("825a"),a=r("50c4"),i=r("a691"),l=r("1d80"),c=r("8aa5"),s=r("0cb2"),u=r("14c3"),m=Math.max,p=Math.min,d=function(e){return void 0===e?e:String(e)};n("replace",2,(function(e,t,r,n){var f=n.REGEXP_REPLACE_SUBSTITUTES_UNDEFINED_CAPTURE,v=n.REPLACE_KEEPS_$0,x=f?"$":"$0";return[function(r,n){var o=l(this),a=void 0==r?void 0:r[e];return void 0!==a?a.call(r,o,n):t.call(String(o),r,n)},function(e,n){if(!f&&v||"string"===typeof n&&-1===n.indexOf(x)){var l=r(t,e,this,n);if(l.done)return l.value}var g=o(e),b=String(this),h="function"===typeof n;h||(n=String(n));var _=g.global;if(_){var F=g.unicode;g.lastIndex=0}var S=[];while(1){var y=u(g,b);if(null===y)break;if(S.push(y),!_)break;var E=String(y[0]);""===E&&(g.lastIndex=c(b,a(g.lastIndex),F))}for(var R="",k=0,$=0;$<S.length;$++){y=S[$];for(var w=String(y[0]),C=m(p(i(y.index),b.length),0),P=[],A=1;A<y.length;A++)P.push(d(y[A]));var I=y.groups;if(h){var N=[w].concat(P,C,b);void 0!==I&&N.push(I);var U=String(n.apply(void 0,N))}else U=s(w,b,C,P,I,n);C>=k&&(R+=b.slice(k,C)+U,k=C+w.length)}return R+b.slice(k)}]}))},7156:function(e,t,r){var n=r("861d"),o=r("d2bb");e.exports=function(e,t,r){var a,i;return o&&"function"==typeof(a=t.constructor)&&a!==r&&n(i=a.prototype)&&i!==r.prototype&&o(e,i),e}},"8aa5":function(e,t,r){"use strict";var n=r("6547").charAt;e.exports=function(e,t,r){return t+(r?n(e,t).length:1)}},9263:function(e,t,r){"use strict";var n=r("ad6d"),o=r("9f7f"),a=r("5692"),i=RegExp.prototype.exec,l=a("native-string-replace",String.prototype.replace),c=i,s=function(){var e=/a/,t=/b*/g;return i.call(e,"a"),i.call(t,"a"),0!==e.lastIndex||0!==t.lastIndex}(),u=o.UNSUPPORTED_Y||o.BROKEN_CARET,m=void 0!==/()??/.exec("")[1],p=s||m||u;p&&(c=function(e){var t,r,o,a,c=this,p=u&&c.sticky,d=n.call(c),f=c.source,v=0,x=e;return p&&(d=d.replace("y",""),-1===d.indexOf("g")&&(d+="g"),x=String(e).slice(c.lastIndex),c.lastIndex>0&&(!c.multiline||c.multiline&&"\n"!==e[c.lastIndex-1])&&(f="(?: "+f+")",x=" "+x,v++),r=new RegExp("^(?:"+f+")",d)),m&&(r=new RegExp("^"+f+"$(?!\\s)",d)),s&&(t=c.lastIndex),o=i.call(p?r:c,x),p?o?(o.input=o.input.slice(v),o[0]=o[0].slice(v),o.index=c.lastIndex,c.lastIndex+=o[0].length):c.lastIndex=0:s&&o&&(c.lastIndex=c.global?o.index+o[0].length:t),m&&o&&o.length>1&&l.call(o[0],r,(function(){for(a=1;a<arguments.length-2;a++)void 0===arguments[a]&&(o[a]=void 0)})),o}),e.exports=c},"9f7f":function(e,t,r){"use strict";var n=r("d039");function o(e,t){return RegExp(e,t)}t.UNSUPPORTED_Y=n((function(){var e=o("a","y");return e.lastIndex=2,null!=e.exec("abcd")})),t.BROKEN_CARET=n((function(){var e=o("^r","gy");return e.lastIndex=2,null!=e.exec("str")}))},ac1f:function(e,t,r){"use strict";var n=r("23e7"),o=r("9263");n({target:"RegExp",proto:!0,forced:/./.exec!==o},{exec:o})},acec:function(e,t,r){"use strict";r.r(t);var n=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("el-card",{staticClass:"box-card"},[r("div",{},[r("el-tabs",{on:{"tab-click":e.handleClick},model:{value:e.activeName,callback:function(t){e.activeName=t},expression:"activeName"}},[r("el-tab-pane",{attrs:{label:"物料码",name:"first"}},[r("CommonPrintMatter")],1),r("el-tab-pane",{attrs:{label:"箱号",name:"second"}},[r("CommonBoxCode")],1),r("el-tab-pane",{attrs:{label:"发货码",name:"fourth"}},[r("CommonDeliverCode")],1)],1)],1)])],1)},o=[],a=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("el-card",{staticClass:"box-card"},[r("div",{},[r("el-form",{ref:"matterFormRef",staticStyle:{padding:"0 60px 0 20px",width:"650px"},attrs:{model:e.matterForm,rules:e.matterFormRules,"label-width":"150px"}},[r("el-form-item",{attrs:{label:"打印个数",prop:"count"}},[r("el-input",{model:{value:e.matterForm.count,callback:function(t){e.$set(e.matterForm,"count",t)},expression:"matterForm.count"}})],1),r("el-form-item",{attrs:{label:"最大位数",prop:"max_digit"}},[r("el-input",{model:{value:e.matterForm.max_digit,callback:function(t){e.$set(e.matterForm,"max_digit",t)},expression:"matterForm.max_digit"}})],1),r("el-form-item",{attrs:{label:"起始值",prop:"initial_value"}},[r("el-input",{model:{value:e.matterForm.initial_value,callback:function(t){e.$set(e.matterForm,"initial_value",t)},expression:"matterForm.initial_value"}})],1),r("el-form-item",{attrs:{label:"规律",prop:"rule"}},[r("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择"},model:{value:e.matterForm.rule,callback:function(t){e.$set(e.matterForm,"rule",t)},expression:"matterForm.rule"}},[r("el-option",{attrs:{label:"递增",value:"递增"}}),r("el-option",{attrs:{label:"递减",value:"递减"}})],1)],1),r("el-form-item",{attrs:{label:"达到极限值重新计数",prop:"again_num"}},[r("el-input",{model:{value:e.matterForm.again_num,callback:function(t){e.$set(e.matterForm,"again_num",t)},expression:"matterForm.again_num"}})],1),r("el-form-item",{attrs:{label:"字首",prop:"prefix"}},[r("el-input",{model:{value:e.matterForm.prefix,callback:function(t){e.$set(e.matterForm,"prefix",t)},expression:"matterForm.prefix"}})],1),r("el-form-item",{attrs:{label:"字尾",prop:"suffix"}},[r("el-input",{model:{value:e.matterForm.suffix,callback:function(t){e.$set(e.matterForm,"suffix",t)},expression:"matterForm.suffix"}})],1)],1),r("div",[r("el-button",{on:{click:e.reset_matterForm}},[e._v("重 置")]),r("el-button",{attrs:{type:"primary"},on:{click:e.save_matterForm}},[e._v("打 印")])],1)],1)])],1)},i=[],l=r("fd03"),c={data:function(){return{matterForm:{count:"5",max_digit:"4",initial_value:"0001",rule:"递增",again_num:"",prefix:"SPR001300-2A001364-CMSS-A01-081021-0001",suffix:""},matterFormBase:{count:"5",max_digit:"4",initial_value:"0001",rule:"递增",again_num:"",prefix:"SPR001300-2A001364-CMSS-A01-081021-0001",suffix:""},matterFormRules:{}}},methods:{reset_matterForm:function(){this.matterForm=JSON.parse(JSON.stringify(this.matterFormBase))},save_matterForm:function(){var e={fileType:"matter_code",stem1:"SUB-ASSHEUH-2A001364-100",stem2:"SPR001300",stem3:"40",stem4:"20",stem5:"00A01",stem6:"00A01"};this.getLogisticPrintApai(e)},getLogisticPrintApai:function(e){var t=this;l["a"].getLogisticPrintApai(e).then((function(e){console.log("打印 新增",e),0==e.code?t.$message({message:e.message,type:"success"}):t.$message({message:e.message,type:"error"})}))}}},s=c,u=r("2877"),m=Object(u["a"])(s,a,i,!1,null,null,null),p=m.exports,d=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("el-card",{staticClass:"box-card"},[r("div",{},[r("el-form",{ref:"boxFormRef",staticStyle:{padding:"0 60px 0 20px",width:"650px"},attrs:{model:e.boxForm,rules:e.boxFormRules,"label-width":"100px"}},[r("el-form-item",{attrs:{label:"起始值",prop:"box_code"}},[r("el-input",{model:{value:e.boxForm.box_code,callback:function(t){e.$set(e.boxForm,"box_code",t)},expression:"boxForm.box_code"}})],1)],1),r("div",[r("el-button",{on:{click:e.reset_boxForm}},[e._v("重 置")]),r("el-button",{attrs:{type:"primary"},on:{click:e.save_boxForm}},[e._v("打 印")])],1)],1)])],1)},f=[];r("5319"),r("ac1f"),r("4d63"),r("25f0");function v(e,t){var r=new Date(e),n={"M+":r.getMonth()+1,"d+":r.getDate(),"h+":r.getHours(),"m+":r.getMinutes(),"s+":r.getSeconds(),"w+":r.getDay(),"q+":Math.floor((r.getMonth()+3)/3),S:r.getMilliseconds()};for(var o in/(y+)/.test(t)&&(t=t.replace(RegExp.$1,(r.getFullYear()+"").substr(4-RegExp.$1.length))),n)"w+"===o?0===n[o]?t=t.replace("w","周日"):1===n[o]?t=t.replace("w","周一"):2===n[o]?t=t.replace("w","周二"):3===n[o]?t=t.replace("w","周三"):4===n[o]?t=t.replace("w","周四"):5===n[o]?t=t.replace("w","周五"):6===n[o]&&(t=t.replace("w","周六")):new RegExp("("+o+")").test(t)&&(t=t.replace(RegExp.$1,1==RegExp.$1.length?n[o]:("00"+n[o]).substr((""+n[o]).length)));return t}var x={data:function(){return{boxForm:{box_code:v(new Date,"yyyyMMdd")+"-"},boxFormBase:{box_code:v(new Date,"yyyyMMdd")+"-"},boxFormRules:{}}},methods:{reset_boxForm:function(){this.boxForm=JSON.parse(JSON.stringify(this.boxFormBase))},save_boxForm:function(){console.log("this.boxForm",this.boxForm)}},mounted:function(){console.log(v(new Date,"yyyyMMdd"))}},g=x,b=Object(u["a"])(g,d,f,!1,null,null,null),h=b.exports,_=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("el-card",{staticClass:"box-card"},[r("div",{},[r("el-form",{ref:"deliverFormRef",staticStyle:{padding:"0 60px 0 20px",width:"650px"},attrs:{model:e.deliverForm,rules:e.deliverFormRules,"label-width":"150px"}},[r("el-form-item",{attrs:{label:"Flex料号",prop:"Itemcode_C_Shipping"}},[r("el-input",{model:{value:e.deliverForm.Itemcode_C_Shipping,callback:function(t){e.$set(e.deliverForm,"Itemcode_C_Shipping",t)},expression:"deliverForm.Itemcode_C_Shipping"}})],1),r("el-form-item",{attrs:{label:"供应商编码",prop:"Supplier"}},[r("el-input",{model:{value:e.deliverForm.Supplier,callback:function(t){e.$set(e.deliverForm,"Supplier",t)},expression:"deliverForm.Supplier"}})],1),r("el-form-item",{attrs:{label:"包装数量",prop:"Package_Qty"}},[r("el-input",{model:{value:e.deliverForm.Package_Qty,callback:function(t){e.$set(e.deliverForm,"Package_Qty",t)},expression:"deliverForm.Package_Qty"}})],1),r("el-form-item",{attrs:{label:"发货总箱数",prop:"No_Ship"}},[r("el-input",{model:{value:e.deliverForm.No_Ship,callback:function(t){e.$set(e.deliverForm,"No_Ship",t)},expression:"deliverForm.No_Ship"}})],1),r("el-form-item",{attrs:{label:"版本",prop:"Rv"}},[r("el-input",{model:{value:e.deliverForm.Rv,callback:function(t){e.$set(e.deliverForm,"Rv",t)},expression:"deliverForm.Rv"}})],1)],1),r("div",[r("el-button",{on:{click:e.reset_deliverForm}},[e._v("重 置")]),r("el-button",{attrs:{type:"primary"},on:{click:e.save_deliverForm}},[e._v("打 印")])],1)],1)])],1)},F=[],S={data:function(){return{deliverForm:{Itemcode_C_Shipping:"SUB-ASSHEUH-2A001364-100",Supplier:"SPR001300",Package_Qty:"40",No_Ship:"20",Rv:"00A01"},deliverFormBase:{Itemcode_C_Shipping:"SUB-ASSHEUH-2A001364-100",Supplier:"SPR001300",Package_Qty:"40",No_Ship:"20",Rv:"00A01"},deliverFormRules:{}}},methods:{reset_deliverForm:function(){this.deliverForm=JSON.parse(JSON.stringify(this.deliverFormBase))},save_deliverForm:function(){console.log("this.deliverForm",this.deliverForm)}}},y=S,E=Object(u["a"])(y,_,F,!1,null,null,null),R=E.exports,k=(r("bc3a"),{components:{CommonPrintMatter:p,CommonBoxCode:h,CommonDeliverCode:R},data:function(){return{activeName:"first"}},methods:{handleClick:function(e,t){console.log(e,t)}},mounted:function(){}}),$=k,w=Object(u["a"])($,n,o,!1,null,null,null);t["default"]=w.exports},ad6d:function(e,t,r){"use strict";var n=r("825a");e.exports=function(){var e=n(this),t="";return e.global&&(t+="g"),e.ignoreCase&&(t+="i"),e.multiline&&(t+="m"),e.dotAll&&(t+="s"),e.unicode&&(t+="u"),e.sticky&&(t+="y"),t}},d784:function(e,t,r){"use strict";r("ac1f");var n=r("6eeb"),o=r("d039"),a=r("b622"),i=r("9263"),l=r("9112"),c=a("species"),s=!o((function(){var e=/./;return e.exec=function(){var e=[];return e.groups={a:"7"},e},"7"!=="".replace(e,"$<a>")})),u=function(){return"$0"==="a".replace(/./,"$0")}(),m=a("replace"),p=function(){return!!/./[m]&&""===/./[m]("a","$0")}(),d=!o((function(){var e=/(?:)/,t=e.exec;e.exec=function(){return t.apply(this,arguments)};var r="ab".split(e);return 2!==r.length||"a"!==r[0]||"b"!==r[1]}));e.exports=function(e,t,r,m){var f=a(e),v=!o((function(){var t={};return t[f]=function(){return 7},7!=""[e](t)})),x=v&&!o((function(){var t=!1,r=/a/;return"split"===e&&(r={},r.constructor={},r.constructor[c]=function(){return r},r.flags="",r[f]=/./[f]),r.exec=function(){return t=!0,null},r[f](""),!t}));if(!v||!x||"replace"===e&&(!s||!u||p)||"split"===e&&!d){var g=/./[f],b=r(f,""[e],(function(e,t,r,n,o){return t.exec===i?v&&!o?{done:!0,value:g.call(t,r,n)}:{done:!0,value:e.call(r,t,n)}:{done:!1}}),{REPLACE_KEEPS_$0:u,REGEXP_REPLACE_SUBSTITUTES_UNDEFINED_CAPTURE:p}),h=b[0],_=b[1];n(String.prototype,e,h),n(RegExp.prototype,f,2==t?function(e,t){return _.call(e,this,t)}:function(e){return _.call(e,this)})}m&&l(RegExp.prototype[f],"sham",!0)}}}]);
//# sourceMappingURL=chunk-6d072ae6.cd335651.js.map