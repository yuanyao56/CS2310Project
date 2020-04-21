<template>
   <q-layout view="hHh lpR fFf">

    <q-page-container>
      <q-page class="flex-container">
        <div class="flex-item" >
          <q-field id="read" label="Current Read" stack-label v-model="curRead">
            {{curRead}}
          </q-field>
        </div>
       <div class="flex-item">
          <q-btn  label="Cold" color="blue" @click="uncomftable(0)"></q-btn>    
          <q-btn  label="HOt" color="red" @click="uncomftable(1)"></q-btn>    
      </div>
      <div class="flex-item">
        <p color="black">{{message}}</p>
      </div>
       </q-page>
    </q-page-container>

  </q-layout>
</template>

<script>
export default {
  data(){
    return{
      value : 10,
      set : 210,
      curRead : '71',
      message : "Ready"
    }
  },

  created () {
     var _this=this
    setInterval((that) => {
       that.$axios.get('http://127.0.0.1:5000/curTemp')
      .then((response) => {
        that.curRead=response.data
      })
      .catch( (error) => {
        console.log(error.response);
      
      });
    }, 5000, this)
  },

  methods:{
    uncomftable(request){
        var navigate = this.$router;
        this.$axios.post('http://127.0.0.1:5000/change',{type:request,angle:this.set})
      .then((response) =>{
        debugger
        console.log("get response")
        console.log(response.data['message'])
        this.message=response.data['message']
      })
      .catch((error)=> {
        console.log("error");   
        console.log(error.response);   
      });
    }
  }

}
</script>



<style scoped>

.flex-container {
  display: flex;
  

  flex-flow: row wrap;
  
  /* Then we define how is distributed the remaining space */
  justify-content: space-around;
  
  padding: 0;
  margin: 0;
  list-style: none;
}

.flex-item {
  padding: 5px;
  width: 200px;
  height: 100px;
  margin-top: 10px;
  line-height: 150px;
  color: black;
  font-weight: bold;
  font-size: 1em;
  text-align: center;
}
</style>