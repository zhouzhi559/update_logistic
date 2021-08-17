(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d21b2d6"],{bf51:function(e,t,r){"use strict";r.r(t);var o=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("el-card",[r("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[r("span",[e._v("工站编号 : "+e._s(e.CurrentUserInfo.work_id))]),r("span",{staticClass:"ml20"},[e._v("工站名称 : "+e._s(e.workStationName))]),r("span",{staticClass:"ml20"},[e._v("工站类型 : "+e._s(e.CurrentUserInfo.work_type))])]),r("el-form",{ref:"formRef",staticStyle:{padding:"0 60px 0 20px",width:"650px"},attrs:{model:e.form,rules:e.formRules,"label-width":"100px"}},[r("el-form-item",{attrs:{prop:"finished_product_code",label:"产品编号",rules:[{required:!0,message:"产品编号不能为空"}]}},[r("el-input",{ref:"firstInput",on:{input:e.inputChange},model:{value:e.form.finished_product_code,callback:function(t){e.$set(e.form,"finished_product_code",t)},expression:"form.finished_product_code"}})],1),e._l(e.form.response_datas,(function(t,o){return r("div",{key:o+" onlyItem"},[r("el-form-item",{attrs:{prop:"response_datas."+o+".matter_id",rules:[{required:!0,message:"物料编码不能为空",trigger:"blur"},{pattern:t.rule,message:"编码需要包含"+t.rule,trigger:"blur"}],label:t.matter_name}},[r("el-input",{ref:"matterInput"+o,refInFor:!0,on:{input:function(r){e.nextFocus("matterInput"+(o+1),o,t.matter_code,r)}},model:{value:t.matter_id,callback:function(r){e.$set(t,"matter_id",r)},expression:"item.matter_id"}})],1)],1)})),r("el-form-item",{attrs:{label:"检验结果",prop:"test_result"}},[r("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择"},model:{value:e.form.test_result,callback:function(t){e.$set(e.form,"test_result",t)},expression:"form.test_result"}},[r("el-option",{attrs:{label:"合格",value:"合格"}}),r("el-option",{attrs:{label:"不合格",value:"不合格"}})],1)],1),"不合格"==e.form.test_result?r("el-form-item",{attrs:{label:"备注",prop:"description"}},[r("el-input",{attrs:{type:"textarea"},model:{value:e.form.description,callback:function(t){e.$set(e.form,"description",t)},expression:"form.description"}})],1):e._e()],2),r("div",[r("el-button",{on:{click:e.resetForm}},[e._v("重 置")]),r("el-button",{attrs:{type:"primary"},on:{click:e.dialogSave}},[e._v("确 定")])],1)],1)],1)},s=[],a=r("1da1"),i=r("5530"),n=(r("96cf"),r("159b"),r("fd03")),c=r("2f62"),m={name:"MissStation",data:function(){return{timeout:"",QualifiedFlag:!1,form:{product_plan_code:"",finished_product_code:"",response_datas:[],test_result:"合格"},formBase:{product_plan_code:"",finished_product_code:"",response_datas:[],test_result:"合格"},formRules:{test_result:[{required:!0,message:"请选择检验结果",trigger:"change"}]},response_datasRules:{matter_id:[{required:!0,message:"数量不能为空",trigger:"blur"}]}}},computed:Object(i["a"])({},Object(c["c"])(["ProductPlanCodeNameList","MatterCodeNameList","BomMatterCodeNameList","WorkCodeNameList","CurrentUserInfo"])),methods:Object(i["a"])(Object(i["a"])({},Object(c["b"])(["getLogisticProductPlanCodeName","getLogisticMatterNameCode","getLogisticBomMatterCodeName","getLogisticWorkCodeName"])),{},{inputChange:function(e){var t=this,r=e;this.timeout&&clearTimeout(this.timeout),this.timeout=setTimeout((function(){if(t.form.finished_product_code==r&&t.form.finished_product_code){var e={finished_product_code:t.form.finished_product_code};n["a"].getLogisticQualifiedMatterCode(e).then((function(e){console.log("寻找此工站的上一站的物料是否合格接口： 查询",e),0==e.code?t.QualifiedFlag=!0:t.$message({message:e.message,type:"error"})}))}}),500)},nextFocus:function(e,t,r,o){var s=this;this.form.response_datas[t].matter_id;this.timeout&&clearTimeout(this.timeout),this.timeout=setTimeout((function(){t<s.form.response_datas.length-1&&s.$nextTick((function(){s.$refs[e][0].focus()}))}),500)},getLogisticWorkStationGetData:function(){var e=this;return Object(a["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,e.getLogisticBomMatterCodeName();case 2:n["a"].getLogisticWorkStationGetData().then((function(t){if(console.log("通过工站获取BOM产品物料： 查询",t),console.log("产品　物料code和名称接口 查询 BomMatterCodeNameList",e.BomMatterCodeNameList),0==t.code){var r=t.data[0].response_datas,o=[];r.forEach((function(t,r){e.BomMatterCodeNameList.forEach((function(e){t.matter_code==e.matter_code&&(t.matter_name=e.matter_name,t.rule=e.rule)}))}));for(var s=0;s<r.length;s++)for(var a=0;a<r[s].install_number;a++)o.push({matter_name:r[s].matter_name,matter_code:r[s].matter_code,matter_id:r[s].matter_id,rule:r[s].rule});e.form.response_datas=o}else e.$message({message:t.message,type:"error"})}));case 3:case"end":return t.stop()}}),t)})))()},postLogisticProductTransitInfo:function(e){var t=this;n["a"].postLogisticProductTransitInfo(e).then((function(e){console.log("产品过站 新增",e),0==e.code?(t.resetForm(),t.$message({message:e.message,type:"success"})):t.$message({message:e.message,type:"error"})}))},resetForm:function(){var e=this;this.form=JSON.parse(JSON.stringify(this.formBase)),this.getLogisticWorkStationGetData(),this.$nextTick((function(){e.$refs.formRef.clearValidate()}))},dialogSave:function(){var e=this;this.$refs.formRef.validate((function(t){t?(console.log("产品过站",e.form),e.QualifiedFlag?e.postLogisticProductTransitInfo(e.form):e.$message({message:"该产品上一工站不合格",type:"error"})):e.$message({message:"请修改正确的数据格式！",type:"warning"})}))}}),mounted:function(){var e=this;this.getLogisticWorkStationGetData(),this.getLogisticWorkCodeName(),this.WorkCodeNameList.forEach((function(t){e.CurrentUserInfo.work_id==t.work_id&&(e.workStationName=t.work_name)})),this.$nextTick((function(){e.$refs.firstInput.focus()}))}},u=m,d=r("2877"),l=Object(d["a"])(u,o,s,!1,null,null,null);t["default"]=l.exports}}]);
//# sourceMappingURL=chunk-2d21b2d6.a07427b5.js.map