(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-6aab7636"],{"0b3e":function(t,e,s){"use strict";var o=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",[s("el-card",[s("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[s("span",[t._v("成品"+t._s(t.cardTitle))])]),s("el-form",{ref:"formRef",staticStyle:{padding:"0 60px 0 20px",width:"650px"},attrs:{model:t.form,rules:t.formRules,"label-width":"100px"}},[s("el-form-item",{attrs:{prop:"count",label:t.cardTitle+"数量"}},[s("el-input",{ref:"firstInput",on:{input:t.inputChange},model:{value:t.form.count,callback:function(e){t.$set(t.form,"count",t._n(e))},expression:"form.count"}})],1),t._l(t.form.response_datas,(function(e,o){return s("div",{key:o+" onlyItem"},[s("el-form-item",{attrs:{prop:"response_datas."+o+".pack_id",rules:[],label:"包装编码"}},[s("el-input",{ref:"finishedProductCode"+o,refInFor:!0,on:{input:function(s){t.nextFocus("finishedProductCode"+(o+1),o,e.pack_id)}},model:{value:e.pack_id,callback:function(s){t.$set(e,"pack_id",s)},expression:"item.pack_id"}})],1)],1)}))],2),s("div",[s("el-button",{on:{click:t.resetForm}},[t._v("重 置")]),s("el-button",{attrs:{type:"primary"},on:{click:t.dialogSave}},[t._v("确 定")])],1)],1)],1)},r=[],n=s("fd03"),a={name:"MissStation",props:{formStatus:{type:String,default:""},cardTitle:{type:String,default:""}},data:function(){return{timeout:"",form:{count:"",status:"",response_datas:[]},formBase:{count:"",status:"",response_datas:[]},formRules:{count:[{required:!0,message:"请输入数量",trigger:"blur"},{type:"number",message:"数量必须为数值",trigger:"blur"}]}}},computed:{},methods:{inputChange:function(){this.form.response_datas=[];for(var t=0;t<this.form.count;t++)this.form.response_datas.push({pack_id:""})},nextFocus:function(t,e,s){var o=this;this.timeout&&clearTimeout(this.timeout),this.timeout=setTimeout((function(){e<o.form.response_datas.length-1?o.$nextTick((function(){o.$refs[t][0].focus()})):console.log(5789)}),500)},getLogisticstockInStockOut:function(t){var e=this;n["a"].getLogisticstockInStockOut(t).then((function(t){console.log("产品过站 新增",t),0==t.code?(e.form=JSON.parse(JSON.stringify(e.formBase)),e.$message({message:t.message,type:"success"})):e.$message({message:t.message,type:"error"})}))},resetForm:function(){this.form=JSON.parse(JSON.stringify(this.formBase))},dialogSave:function(){var t=this;console.log("this.form",this.form),this.$refs.formRef.validate((function(e){if(e){console.log("产品过站",t.form);var s=JSON.parse(JSON.stringify(t.form));s.status=t.formStatus,s.response_datas=JSON.stringify(t.form.response_datas),console.log("paramsparams",s),t.getLogisticstockInStockOut(s)}else t.$message({message:"请修改正确的数据格式！",type:"warning"})}))}},mounted:function(){var t=this;this.$nextTick((function(){t.$refs.firstInput.focus()}))}},i=a,c=s("2877"),u=Object(c["a"])(i,o,r,!1,null,null,null);e["a"]=u.exports},"57c2":function(t,e,s){"use strict";s.r(e);var o=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("FinishedProductStorageDispatch",{attrs:{formStatus:"出库",cardTitle:"出库"}})},r=[],n=s("0b3e"),a={name:"UserLogin",data:function(){return{}},components:{FinishedProductStorageDispatch:n["a"]}},i=a,c=s("2877"),u=Object(c["a"])(i,o,r,!1,null,null,null);e["default"]=u.exports}}]);
//# sourceMappingURL=chunk-6aab7636.281fadef.js.map