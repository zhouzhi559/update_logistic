(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-b55f978c"],{"72f9":function(e,t,a){"use strict";a.r(t);var l=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",{staticClass:"formDiv"},[a("el-form",{staticClass:"demo-form-inline",attrs:{inline:!0}},[a("el-form-item",{attrs:{label:"数据库名称"}},[a("el-input",{attrs:{placeholder:"请输入"},model:{value:e.search_database_name,callback:function(t){e.search_database_name=t},expression:"search_database_name"}})],1),a("el-form-item",{attrs:{label:"物料类型"}},[a("el-select",{attrs:{placeholder:"请选择"},model:{value:e.search_database_type,callback:function(t){e.search_database_type=t},expression:"search_database_type"}},[a("el-option",{attrs:{label:"全部",value:"全部"}}),a("el-option",{attrs:{label:"MySQL",value:"MySQL"}}),a("el-option",{attrs:{label:"SQLServer",value:"SQLServer"}}),a("el-option",{attrs:{label:"Oracle",value:"Oracle"}})],1)],1),a("el-form-item",{staticStyle:{"margin-left":"20px !important"}},[a("el-button",{attrs:{type:"primary",size:"medium"},on:{click:e.searchBtn}},[e._v("查询")]),a("el-button",{attrs:{size:"medium"},on:{click:function(t){return e.resetForm()}}},[e._v("重置")])],1)],1)],1),a("el-card",{staticClass:"box-card mt20"},[a("div",{},[a("el-form",{staticClass:"demo-form-inline",attrs:{inline:!0}},[a("el-form-item",[a("el-button",{attrs:{type:"primary",size:"medium",plain:""},on:{click:e.addBtn}},[a("i",{staticClass:"el-icon-plus"}),e._v(" 新增")])],1)],1),a("ELTable",{attrs:{tableCol:e.tableCol,tableData:e.tableData}})],1)]),a("el-dialog",{attrs:{title:e.dialogTitle,width:"600px",visible:e.dialogFlag,"close-on-click-modal":!1},on:{"update:visible":function(t){e.dialogFlag=t}}},[a("el-form",{ref:"dialogFormRef",staticStyle:{padding:"0 60px 0 20px"},attrs:{model:e.dialogForm,rules:e.dialogFormRules,"label-width":"100px"}},[a("el-form-item",{attrs:{label:"数据库名称",prop:"db_name"}},[a("el-input",{model:{value:e.dialogForm.db_name,callback:function(t){e.$set(e.dialogForm,"db_name",t)},expression:"dialogForm.db_name"}})],1),a("el-form-item",{attrs:{label:"数据库类型",prop:"db_type"}},[a("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择"},model:{value:e.dialogForm.db_type,callback:function(t){e.$set(e.dialogForm,"db_type",t)},expression:"dialogForm.db_type"}},[a("el-option",{attrs:{label:"全部",value:"全部"}}),a("el-option",{attrs:{label:"MySQL",value:"MySQL"}}),a("el-option",{attrs:{label:"SQLServer",value:"SQLServer"}}),a("el-option",{attrs:{label:"Oracle",value:"Oracle"}})],1)],1),a("el-form-item",{attrs:{label:"状态",prop:"db_status"}},[a("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择"},model:{value:e.dialogForm.db_status,callback:function(t){e.$set(e.dialogForm,"db_status",t)},expression:"dialogForm.db_status"}},[a("el-option",{attrs:{label:"启用",value:"启用"}}),a("el-option",{attrs:{label:"禁用",value:"禁用"}})],1)],1),a("el-form-item",{attrs:{label:"备注",prop:"db_description"}},[a("el-input",{attrs:{type:"textarea"},model:{value:e.dialogForm.db_description,callback:function(t){e.$set(e.dialogForm,"db_description",t)},expression:"dialogForm.db_description"}})],1)],1),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.dialogFlag=!1}}},[e._v("取 消")]),a("el-button",{attrs:{type:"primary"},on:{click:e.dialogSave}},[e._v("确 定")])],1)],1)],1)},i=[],o=a("a927"),n=(a("fd03"),{name:"Database",components:{ELTable:o["a"]},data:function(){return{search_database_name:"",search_database_type:"",dialogTitle:"",dialogFlag:!1,dialogForm:{db_code:"",db_name:"",db_type:"",db_status:"",db_description:""},dialogFormBase:{db_code:"",db_name:"",db_type:"",db_status:"",db_description:""},dialogFormRules:{db_name:[{required:!0,message:"请输入数据库名称",trigger:"blur"}],db_type:[{required:!0,message:"请选择数据库类型",trigger:"blur"}],db_status:[{required:!0,message:"请选择状态",trigger:"change"}]},tableCol:[{label:"数据库名称",field:"db_name",align:"center"},{label:"数据库类型",field:"db_type",align:"center"},{label:"状态",field:"db_status",align:"center"},{label:"备注",field:"db_description",align:"center"},{label:"操作",colType:"solt",align:"center",option:[{label:"修改",event:this.colEditBtn},{label:"删除",event:this.colDeleteBtn}]}],tableData:[]}},methods:{searchBtn:function(){this.listQuery.page=1,console.log("submit!")},resetForm:function(){this.user_id=""},addBtn:function(){this.dialogTitle="新增数据库",this.dialogFlag=!0},dialogSave:function(){var e=this;console.log(123),this.$refs.dialogFormRef.validate((function(t){t||e.$message({message:"请修改正确的数据格式！",type:"warning"})}))}}}),r=n,s=a("2877"),d=Object(s["a"])(r,l,i,!1,null,"6a6d370d",null);t["default"]=d.exports},a927:function(e,t,a){"use strict";var l=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("el-table",{staticStyle:{width:"100%"},attrs:{data:e.tableData,"header-cell-style":{background:"#eef1f6",color:"#606266"}},on:{"selection-change":e.handleSelectionChange}},[e.isShowSelect?a("el-table-column",{attrs:{type:"selection",width:"55"}}):e._e(),e._l(e.tableCol,(function(t,l){return["solt"==t.colType?a("el-table-column",{key:l+"only",attrs:{prop:t.field,label:t.label,width:t.width,align:t.align?t.align:"left"},scopedSlots:e._u([{key:"default",fn:function(l){return e._l(t.option,(function(t,i){return a("el-button",{key:i+"only",attrs:{type:"text",size:"small"},on:{click:function(e){return t.event(l.row)}}},[e._v(e._s(t.label))])}))}}],null,!0)}):a("el-table-column",{key:l+"only",attrs:{prop:t.field,label:t.label,width:t.width,align:t.align?t.align:"left"}})]}))],2),e.ispagination?a("div",{staticClass:"pagination-wrap"},[a("el-pagination",{attrs:{"current-page":e.listQuery.page,"page-sizes":[5,10,20,30,40,50,100],"page-size":e.listQuery.page_size,layout:"total, sizes, prev, pager, next, jumper",total:e.listQuery.total},on:{"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}})],1):e._e()],1)},i=[],o={name:"ELTable",props:{tableCol:{type:Array,default:function(){return[]}},tableData:{type:Array,default:function(){return[]}},ispagination:{type:Boolean,default:!0},isShowSelect:{type:Boolean,default:!1},listQuery:{type:Object,default:function(){return{page:1,page_size:10,total:0}}}},data:function(){return{}},methods:{handleSizeChange:function(e){this.$emit("sizeChange",e)},handleCurrentChange:function(e){this.$emit("currentChange",e)},handleSelectionChange:function(e){this.$emit("handleSelectionChange",e)}}},n=o,r=a("2877"),s=Object(r["a"])(n,l,i,!1,null,"f6412f26",null);t["a"]=s.exports}}]);
//# sourceMappingURL=chunk-b55f978c.7b1a3f0b.js.map