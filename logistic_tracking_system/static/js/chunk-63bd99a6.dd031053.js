(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-63bd99a6"],{"1bb9":function(e,t,o){"use strict";o("4978")},4978:function(e,t,o){},a434:function(e,t,o){"use strict";var a=o("23e7"),l=o("23cb"),i=o("a691"),s=o("50c4"),r=o("7b0b"),c=o("65f0"),n=o("8418"),d=o("1dde"),u=d("splice"),g=Math.max,h=Math.min,m=9007199254740991,p="Maximum allowed length exceeded";a({target:"Array",proto:!0,forced:!u},{splice:function(e,t){var o,a,d,u,f,_,k=r(this),y=s(k.length),b=l(e,y),w=arguments.length;if(0===w?o=a=0:1===w?(o=0,a=y-b):(o=w-2,a=h(g(i(t),0),y-b)),y+o-a>m)throw TypeError(p);for(d=c(k,a),u=0;u<a;u++)f=b+u,f in k&&n(d,u,k[f]);if(d.length=a,o<a){for(u=b;u<y-a;u++)f=u+a,_=u+o,f in k?k[_]=k[f]:delete k[_];for(u=y;u>y-a+o;u--)delete k[u-1]}else if(o>a)for(u=y-a;u>b;u--)f=u+a-1,_=u+o-1,f in k?k[_]=k[f]:delete k[_];for(u=0;u<o;u++)k[u+b]=arguments[u+2];return k.length=y-a+o,d}})},a927:function(e,t,o){"use strict";var a=function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",[o("el-table",{staticStyle:{width:"100%"},attrs:{data:e.tableData,"header-cell-style":{background:"#eef1f6",color:"#606266"}},on:{"selection-change":e.handleSelectionChange}},[e.isShowSelect?o("el-table-column",{attrs:{type:"selection",width:"55"}}):e._e(),e._l(e.tableCol,(function(t,a){return["solt"==t.colType?o("el-table-column",{key:a+"only",attrs:{prop:t.field,label:t.label,width:t.width,align:t.align?t.align:"left"},scopedSlots:e._u([{key:"default",fn:function(a){return e._l(t.option,(function(t,l){return o("el-button",{key:l+"only",attrs:{type:"text",size:"small"},on:{click:function(e){return t.event(a.row)}}},[e._v(e._s(t.label))])}))}}],null,!0)}):o("el-table-column",{key:a+"only",attrs:{prop:t.field,label:t.label,width:t.width,align:t.align?t.align:"left"}})]}))],2),e.ispagination?o("div",{staticClass:"pagination-wrap"},[o("el-pagination",{attrs:{"current-page":e.listQuery.page,"page-sizes":[5,10,20,30,40,50,100],"page-size":e.listQuery.page_size,layout:"total, sizes, prev, pager, next, jumper",total:e.listQuery.total},on:{"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}})],1):e._e()],1)},l=[],i={name:"ELTable",props:{tableCol:{type:Array,default:function(){return[]}},tableData:{type:Array,default:function(){return[]}},ispagination:{type:Boolean,default:!0},isShowSelect:{type:Boolean,default:!1},listQuery:{type:Object,default:function(){return{page:1,page_size:10,total:0}}}},data:function(){return{}},methods:{handleSizeChange:function(e){this.$emit("sizeChange",e)},handleCurrentChange:function(e){this.$emit("currentChange",e)},handleSelectionChange:function(e){this.$emit("handleSelectionChange",e)}}},s=i,r=o("2877"),c=Object(r["a"])(s,a,l,!1,null,"f6412f26",null);t["a"]=c.exports},f838:function(e,t,o){"use strict";o.r(t);var a=function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",[o("div",{staticClass:"formDiv"},[o("el-form",{staticClass:"demo-form-inline",attrs:{inline:!0}},[o("el-form-item",{attrs:{label:"工站"}},[o("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择"},model:{value:e.listQuery.work_code,callback:function(t){e.$set(e.listQuery,"work_code",t)},expression:"listQuery.work_code"}},e._l(e.WorkCodeNameList,(function(e,t){return o("el-option",{key:t+" dialog",attrs:{label:e.work_name,value:e.work_code}})})),1)],1),o("el-form-item",{attrs:{label:"检验方式"}},[o("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择"},model:{value:e.listQuery.check_method,callback:function(t){e.$set(e.listQuery,"check_method",t)},expression:"listQuery.check_method"}},[o("el-option",{attrs:{label:"抽检",value:"抽检"}}),o("el-option",{attrs:{label:"全检",value:"全检"}})],1)],1),o("el-form-item",{staticStyle:{"margin-left":"20px !important"}},[o("el-button",{attrs:{type:"primary",size:"medium"},on:{click:e.searchBtn}},[e._v("查询")]),o("el-button",{attrs:{size:"medium"},on:{click:function(t){return e.resetForm()}}},[e._v("重置")])],1)],1)],1),o("el-card",{staticClass:"box-card mt20"},[o("div",{},[o("el-form",{staticClass:"demo-form-inline",attrs:{inline:!0}},[o("el-form-item",[o("el-button",{attrs:{type:"primary",size:"medium",plain:""},on:{click:e.addBtn}},[o("i",{staticClass:"el-icon-plus"}),e._v(" 新增")])],1)],1),o("ELTable",{attrs:{tableCol:e.tableCol,tableData:e.tableData,listQuery:e.listQuery,ispagination:e.ispagination},on:{currentChange:e.currentChange,sizeChange:e.sizeChange}})],1)]),o("el-dialog",{attrs:{title:e.dialogTitle,width:"1000px",visible:e.dialogFlag,"close-on-click-modal":!1},on:{"update:visible":function(t){e.dialogFlag=t}}},[o("el-form",{ref:"dialogFormRef",staticStyle:{padding:"0 60px 0 20px"},attrs:{model:e.dialogForm,rules:e.dialogFormRules,"label-width":"100px"}},[o("el-row",[o("p",{staticClass:"dialog-title"},[e._v("基本信息")]),o("el-row",{attrs:{gutter:20}},[o("el-col",{attrs:{span:12}},[o("el-form-item",{attrs:{label:"工站",prop:"rule"}},[o("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择"},model:{value:e.dialogForm.work_code,callback:function(t){e.$set(e.dialogForm,"work_code",t)},expression:"dialogForm.work_code"}},e._l(e.WorkCodeNameList,(function(e,t){return o("el-option",{key:t+" dialog",attrs:{label:e.work_name,value:e.work_code}})})),1)],1)],1),o("el-col",{attrs:{span:12}},[o("el-form-item",{attrs:{label:"检验方式",prop:"check_method"}},[o("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择"},model:{value:e.dialogForm.check_method,callback:function(t){e.$set(e.dialogForm,"check_method",t)},expression:"dialogForm.check_method"}},[o("el-option",{attrs:{label:"抽检",value:"抽检"}}),o("el-option",{attrs:{label:"全检",value:"全检"}})],1)],1)],1)],1),o("p",{staticClass:"dialog-title"},[e._v("检验参数")]),o("el-button",{attrs:{type:"primary",size:"small",plain:""},on:{click:function(t){return e.AddListRow()}}},[e._v("添加参数")]),o("el-table",{staticClass:"dialogTable",staticStyle:{width:"100%"},attrs:{data:e.dialogForm.response_datas,height:"240"}},[o("el-table-column",{attrs:{fixed:"left",label:"参数",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[o("el-form-item",{attrs:{prop:"response_datas."+t.$index+".test_parameter"}},[o("el-input",{model:{value:t.row.test_parameter,callback:function(o){e.$set(t.row,"test_parameter",o)},expression:"scope.row.test_parameter"}})],1)]}}])}),o("el-table-column",{attrs:{label:"参数值",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[o("el-form-item",{attrs:{prop:"response_datas."+t.$index+".test_parameter_count"}},[o("el-input",{model:{value:t.row.test_parameter_count,callback:function(o){e.$set(t.row,"test_parameter_count",o)},expression:"scope.row.test_parameter_count"}})],1)]}}])}),o("el-table-column",{attrs:{label:"操作",width:"80",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[o("el-form-item",[o("el-button",{attrs:{size:"small",type:"danger",plain:""},on:{click:function(o){return e.handleDelete(t.$index,t.row)}}},[e._v("删除")])],1)]}}])})],1)],1)],1),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(t){e.dialogFlag=!1}}},[e._v("取 消")]),o("el-button",{attrs:{type:"primary"},on:{click:e.dialogSave}},[e._v("确 定")])],1)],1)],1)},l=[],i=o("1da1"),s=o("5530"),r=(o("96cf"),o("159b"),o("a434"),o("a927")),c=o("fd03"),n=o("2f62"),d={name:"CheckList",components:{ELTable:r["a"]},data:function(){return{listQuery:{prodect_code:"",work_code:"",production_code:"",check_method:"",page:1,page_size:10,total:0},listQueryBase:{prodect_code:"",work_code:"",production_code:"",check_method:"",page:1,page_size:10,total:0},ispagination:!0,dialogTitle:"",dialogFlag:!1,dialogForm:{check_code:"",prodect_code:"",production_code:"",check_method:"",response_datas:[{test_code:"",test_parameter:"",test_parameter_count:"",test_status:""}]},dialogFormBase:{check_code:"",prodect_code:"",production_code:"",check_method:"",response_datas:[{test_code:"",test_parameter:"",test_parameter_count:"",test_status:""}]},dialogFormRules:{},tableCol:[{label:"工站名称",field:"work_name",align:"center"},{label:"检验方式",field:"check_method",align:"center"},{label:"操作",colType:"solt",align:"center",option:[{label:"修改",event:this.colEditBtn},{label:"删除",event:this.colDeleteBtn}]}],tableData:[]}},computed:Object(s["a"])({},Object(n["c"])(["ProductCodeNameList","WorkCodeNameList"])),methods:Object(s["a"])(Object(s["a"])({},Object(n["b"])(["getLogisticProductCodeName","getLogisticWorkCodeName"])),{},{searchBtn:function(){this.listQuery.page=1,this.getLogisticCheckProductDeal(this.listQuery)},resetForm:function(){this.listQuery=JSON.parse(JSON.stringify(this.listQueryBase)),this.getLogisticCheckProductDeal(this.listQuery)},currentChange:function(e){this.listQuery.page=e,this.getLogisticCheckProductDeal(this.listQuery)},sizeChange:function(e){this.listQuery.page=1,this.listQuery.page_size=e,this.getLogisticCheckProductDeal(this.listQuery)},getLogisticCheckProductDeal:function(e){var t=this;return Object(i["a"])(regeneratorRuntime.mark((function o(){return regeneratorRuntime.wrap((function(o){while(1)switch(o.prev=o.next){case 0:return o.next=2,t.getLogisticWorkCodeName();case 2:c["a"].getLogisticCheckProductDeal(e).then((function(e){if(console.log("检验参数 查询",e),0==e.code){var o=e.data.data;o.forEach((function(e){t.WorkCodeNameList.forEach((function(t){e.work_code==t.work_code&&(e.work_name=t.work_name)}))})),t.tableData=o,t.listQuery.total=e.data.total}else t.$message({message:e.message,type:"error"})}));case 3:case"end":return o.stop()}}),o)})))()},postLogisticCheckProductDeal:function(e){var t=this;c["a"].postLogisticCheckProductDeal(e).then((function(e){console.log("检验参数 新增",e),0==e.code?(t.dialogFlag=!1,t.getLogisticCheckProductDeal(t.listQuery),t.$message({message:e.message,type:"success"})):t.$message({message:e.message,type:"error"})}))},colEditBtn:function(e){var t=this;console.log(e),this.dialogTitle="修改检验参数",this.dialogFlag=!0,this.$nextTick((function(){t.$refs.dialogFormRef.clearValidate()})),this.dialogForm={check_code:e.check_code,prodect_code:e.prodect_code,production_code:e.production_code,work_code:e.work_code,check_method:e.check_method,response_datas:e.response_datas}},getLogisticPutCheckProductDeal:function(e){var t=this;c["a"].getLogisticPutCheckProductDeal(e).then((function(e){console.log("修改检验参数 修改",e),0==e.code?(t.dialogFlag=!1,t.getLogisticCheckProductDeal(t.listQuery),t.$message({message:e.message,type:"success"})):t.$message({message:e.message,type:"error"})}))},addBtn:function(){var e=this;this.dialogTitle="新增检验参数",this.dialogFlag=!0,this.$nextTick((function(){e.$refs.dialogFormRef.clearValidate()})),this.dialogForm=JSON.parse(JSON.stringify(this.dialogFormBase))},AddListRow:function(){this.dialogForm.response_datas.push({test_parameter:"",test_parameter_count:"",test_status:""})},dialogSave:function(){var e=this;this.$refs.dialogFormRef.validate((function(t){t?"新增检验参数"==e.dialogTitle?(console.log("新增检验参数",e.dialogForm),e.postLogisticCheckProductDeal(e.dialogForm)):(console.log("修改检验参数",e.dialogForm),e.dialogForm.response_datas=JSON.stringify(e.dialogForm.response_datas),e.getLogisticPutCheckProductDeal(e.dialogForm)):e.$message({message:"请修改正确的数据格式！",type:"warning"})}))},getLogisticDeleteCheckProductDeal:function(e){var t=this;c["a"].getLogisticDeleteCheckProductDeal(e).then((function(e){console.log("检验参数 删除",e),0==e.code?(t.getLogisticCheckProductDeal(t.listQuery),t.$message({message:e.message,type:"success"})):t.$message({message:e.message,type:"error"})}))},handleDelete:function(e,t){var o=this;console.log(e),console.log(t),console.log("rowData.test_coderowData.test_code",t.test_code),t.test_code?this.$confirm("确定执行删除操作吗？","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then((function(){var a={check_code:t.check_code,response_datas:JSON.stringify([{test_code:t.test_code}])};o.getLogisticDeleteCheckProductDeal(a),o.dialogForm.response_datas.splice(e,1)})):this.dialogForm.response_datas.splice(e,1)},colDeleteBtn:function(e){var t=this;this.$confirm("确定执行删除操作吗？","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then((function(){var o={check_code:e.check_code,response_datas:JSON.stringify([])};t.getLogisticDeleteCheckProductDeal(o)}))}}),mounted:function(){this.getLogisticCheckProductDeal(this.listQuery)}},u=d,g=(o("1bb9"),o("2877")),h=Object(g["a"])(u,a,l,!1,null,"19252cb0",null);t["default"]=h.exports}}]);
//# sourceMappingURL=chunk-63bd99a6.dd031053.js.map