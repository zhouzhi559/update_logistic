(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-b55e2874"],{"7cc1":function(e,t,a){"use strict";a.r(t);var l=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("CommonProductMatterSearch")},o=[],i=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",{staticClass:"formDiv"},[a("el-form",{staticClass:"demo-form-inline",attrs:{inline:!0}},[a("el-form-item",{attrs:{label:"产品编号"}},[a("el-input",{model:{value:e.listQuery.finished_product_code,callback:function(t){e.$set(e.listQuery,"finished_product_code",t)},expression:"listQuery.finished_product_code"}})],1),a("el-form-item",{attrs:{label:"物料编号"}},[a("el-input",{model:{value:e.listQuery.matter_id,callback:function(t){e.$set(e.listQuery,"matter_id",t)},expression:"listQuery.matter_id"}})],1),a("el-form-item",{staticStyle:{"margin-left":"20px !important"}},[a("el-button",{attrs:{type:"primary",size:"medium"},on:{click:e.searchBtn}},[e._v("查询")]),a("el-button",{attrs:{size:"medium"},on:{click:function(t){return e.resetForm()}}},[e._v("重置")])],1)],1)],1),a("el-card",{staticClass:"box-card mt20"},[a("div",{},[a("el-form",{staticClass:"demo-form-inline",attrs:{inline:!0}}),a("ELTable",{attrs:{tableCol:e.tableCol,tableData:e.tableData,listQuery:e.listQuery,ispagination:e.ispagination},on:{currentChange:e.currentChange,sizeChange:e.sizeChange}})],1)]),a("el-dialog",{attrs:{title:e.dialogTitle,width:"1000px",visible:e.dialogFlag,"close-on-click-modal":!1},on:{"update:visible":function(t){e.dialogFlag=t}}},[a("el-form",{ref:"dialogFormRef",staticStyle:{padding:"0 60px 0 20px"},attrs:{model:e.dialogForm,rules:e.dialogFormRules,"label-width":"100px"}},[a("el-row",[a("p",{staticClass:"dialog-title"},[e._v("基本信息")]),a("el-row",{attrs:{gutter:20}},[a("el-col",{attrs:{span:12}},[a("el-form-item",{attrs:{label:"产品名称",prop:"product_name"}},[a("el-input",{attrs:{readonly:""},model:{value:e.dialogForm.product_name,callback:function(t){e.$set(e.dialogForm,"product_name",t)},expression:"dialogForm.product_name"}})],1),a("el-form-item",{attrs:{label:"包装编码",prop:"pack_id"}},[a("el-input",{attrs:{readonly:""},model:{value:e.dialogForm.pack_id,callback:function(t){e.$set(e.dialogForm,"pack_id",t)},expression:"dialogForm.pack_id"}})],1),a("el-form-item",{attrs:{label:"状态",prop:"status"}},[a("el-input",{attrs:{readonly:""},model:{value:e.dialogForm.status,callback:function(t){e.$set(e.dialogForm,"status",t)},expression:"dialogForm.status"}})],1)],1),a("el-col",{attrs:{span:12}},[a("el-form-item",{attrs:{label:"规格型号",prop:"rule"}},[a("el-input",{attrs:{readonly:""},model:{value:e.dialogForm.rule,callback:function(t){e.$set(e.dialogForm,"rule",t)},expression:"dialogForm.rule"}})],1),a("el-form-item",{attrs:{label:"产品编号",prop:"finished_product_code"}},[a("el-input",{attrs:{readonly:""},model:{value:e.dialogForm.finished_product_code,callback:function(t){e.$set(e.dialogForm,"finished_product_code",t)},expression:"dialogForm.finished_product_code"}})],1),a("el-form-item",{attrs:{label:"时间",prop:"enter_time"}},[a("el-input",{attrs:{readonly:""},model:{value:e.dialogForm.enter_time,callback:function(t){e.$set(e.dialogForm,"enter_time",t)},expression:"dialogForm.enter_time"}})],1)],1)],1),a("p",{staticClass:"dialog-title"},[e._v("物料明细")]),a("el-table",{staticClass:"dialogTable",staticStyle:{width:"100%"},attrs:{data:e.dialogForm.tableData,height:"300"}},[a("el-table-column",{attrs:{prop:"matter_name",label:"物料名称",align:"center"}}),a("el-table-column",{attrs:{prop:"matter_id",label:"物料编号",align:"center"}}),a("el-table-column",{attrs:{prop:"rule",label:"规格型号",align:"center"}}),a("el-table-column",{attrs:{prop:"matter_category",label:"类型",align:"center"}}),a("el-table-column",{attrs:{prop:"product_time",label:"入库时间",align:"center"}}),a("el-table-column",{attrs:{prop:"work_name",label:"经过工站",align:"center"}}),a("el-table-column",{attrs:{prop:"user_name",label:"过站人员",align:"center"}}),a("el-table-column",{attrs:{prop:"out_time",label:"出站时间",align:"center"}})],1)],1)],1),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.dialogFlag=!1}}},[e._v("确 定")])],1)],1)],1)},r=[],n=a("1da1"),s=(a("96cf"),a("159b"),a("a927")),c=a("fd03"),d={name:"MatterProductSearch",components:{ELTable:s["a"]},data:function(){return{dialogFlag:!1,listQuery:{finished_product_code:"",matter_id:"",page:1,page_size:10,total:0},listQueryBase:{finished_product_code:"",matter_id:"",page:1,page_size:10,total:0},dialogForm:{product_name:"",prodect_code:"",finished_product_code:"",status:"",rule:"",pack_id:"",enter_time:"",tableData:[],response_datas:[]},dialogFormBase:{product_name:"",prodect_code:"",finished_product_code:"",status:"",rule:"",pack_id:"",enter_time:"",tableData:[],response_datas:[]},ispagination:!0,tableCol:[{label:"产品名称",field:"product_name",align:"center"},{label:"产品编号",field:"finished_product_code",align:"center"},{label:"规格型号",field:"rule",align:"center"},{label:"包装编码",field:"pack_id",align:"center"},{label:"状态",field:"status",align:"center"},{label:"时间",field:"enter_time",align:"center"},{label:"操作",colType:"solt",align:"center",option:[{label:"详情",event:this.colDetailBtn}]}],tableData:[],NoPageMatterData:[]}},computed:{},methods:{getLogisticNoPageMatterSearch:function(){var e=this;c["a"].getLogisticNoPageMatterSearch().then((function(t){console.log("通过产品编号 查询 物料",t),0==t.code?e.NoPageMatterData=t.data.data:e.$message({message:t.message,type:"error"})}))},colDetailBtn:function(e){var t=this;console.log(e),this.dialogTitle="产品详情",this.dialogFlag=!0;var a=[];e.response_datas.forEach((function(e){console.log(e),t.NoPageMatterData.forEach((function(l){e==l.matter_id&&(t.PersonCodeNameList.forEach((function(e){l.user_code==e.user_code&&(l.user_name=e.user_name)})),a.push(l))}))})),console.log("dialogTbaleData",a),this.dialogForm={prodect_code:e.prodect_code,product_id:e.product_id,pack_id:e.pack_id,enter_time:e.enter_time,product_name:e.product_name,rule:e.rule,finished_product_code:e.finished_product_code,status:e.status,tableData:a,response_datas:e.response_datas}},searchBtn:function(){this.listQuery.page=1,this.getLogisticProductInfoSearch(this.listQuery)},resetForm:function(){this.listQuery=JSON.parse(JSON.stringify(this.listQueryBase)),this.getLogisticProductInfoSearch(this.listQuery)},currentChange:function(e){this.listQuery.page=e,this.getLogisticProductInfoSearch(this.listQuery)},sizeChange:function(e){this.listQuery.page=1,this.listQuery.page_size=e,this.getLogisticProductInfoSearch(this.listQuery)},getLogisticProductInfoSearch:function(e){var t=this;return Object(n["a"])(regeneratorRuntime.mark((function a(){return regeneratorRuntime.wrap((function(a){while(1)switch(a.prev=a.next){case 0:c["a"].getLogisticProductInfoSearch(e).then((function(e){console.log("过站查询 查询",e),0==e.code?(t.tableData=e.data.data,t.listQuery.total=e.data.total):t.$message({message:e.message,type:"error"})}));case 1:case"end":return a.stop()}}),a)})))()}},mounted:function(){this.getLogisticProductInfoSearch(this.listQuery),this.getLogisticNoPageMatterSearch()}},u=d,p=a("2877"),g=Object(p["a"])(u,i,r,!1,null,null,null),m=g.exports,f={name:"",components:{CommonProductMatterSearch:m}},h=f,_=Object(p["a"])(h,l,o,!1,null,null,null);t["default"]=_.exports},a927:function(e,t,a){"use strict";var l=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("el-table",{staticStyle:{width:"100%"},attrs:{data:e.tableData,"header-cell-style":{background:"#eef1f6",color:"#606266"}},on:{"selection-change":e.handleSelectionChange}},[e.isShowSelect?a("el-table-column",{attrs:{type:"selection",width:"55"}}):e._e(),e._l(e.tableCol,(function(t,l){return["solt"==t.colType?a("el-table-column",{key:l+"only",attrs:{prop:t.field,label:t.label,width:t.width,align:t.align?t.align:"left"},scopedSlots:e._u([{key:"default",fn:function(l){return e._l(t.option,(function(t,o){return a("el-button",{key:o+"only",attrs:{type:"text",size:"small"},on:{click:function(e){return t.event(l.row)}}},[e._v(e._s(t.label))])}))}}],null,!0)}):a("el-table-column",{key:l+"only",attrs:{prop:t.field,label:t.label,width:t.width,align:t.align?t.align:"left"}})]}))],2),e.ispagination?a("div",{staticClass:"pagination-wrap"},[a("el-pagination",{attrs:{"current-page":e.listQuery.page,"page-sizes":[5,10,20,30,40,50,100],"page-size":e.listQuery.page_size,layout:"total, sizes, prev, pager, next, jumper",total:e.listQuery.total},on:{"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}})],1):e._e()],1)},o=[],i={name:"ELTable",props:{tableCol:{type:Array,default:function(){return[]}},tableData:{type:Array,default:function(){return[]}},ispagination:{type:Boolean,default:!0},isShowSelect:{type:Boolean,default:!1},listQuery:{type:Object,default:function(){return{page:1,page_size:10,total:0}}}},data:function(){return{}},methods:{handleSizeChange:function(e){this.$emit("sizeChange",e)},handleCurrentChange:function(e){this.$emit("currentChange",e)},handleSelectionChange:function(e){this.$emit("handleSelectionChange",e)}}},r=i,n=a("2877"),s=Object(n["a"])(r,l,o,!1,null,"f6412f26",null);t["a"]=s.exports}}]);
//# sourceMappingURL=chunk-b55e2874.307198be.js.map