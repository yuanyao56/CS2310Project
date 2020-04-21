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
         <q-knob
        v-if="mode"
      v-model="angle"
      :angle="30"
      size="100px"
      :thickness="0.22"
      color= 'grey-3'
      track-color="red"
      class="q-ma-md"
      id="knob1"
      
      @change="check(angle)"
    ></q-knob>
     <q-knob
        v-else
        
      v-model="angle"
      :angle="320"
      size="100px"
      :thickness="0.22"
      color= 'blue'
      track-color="grey-3"
      class="q-ma-md"
      id="knob1"
      @change="check(angle)"
    ></q-knob>
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
      message : "Ready",
       angle:1,
      mode : false
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
        this.$axios.post('http://127.0.0.1:5000/change',{type:request,angle:this.set})
      .then((response) =>{
        debugger
        if(response.data['change']=="1"){
          if(this.mode){
          //change to cool
          this.mode=false
          }else{
            //change to
            this.mode=true
          }
            this.message=response.data['message']
            console.log(response.data['angle'])
            if(this.mode){
            this.angle=100-response.data['angle']
            }else{
                this.angle=response.data['angle']
            }
            
        }else{
          console.log("unchange")
          this.message=response.data['message']
        }
      })
      .catch((error)=> {
        console.log(error.response);   
      });
    },

   check(newangle){
       if(this.mode){
        if(newangle<50){
           this.angle=50
        }
       }else{
       
         if (newangle>50&&newangle<100){
          this.angle=50
        }
       }
     },
     changeMode(){
       if(this.mode){
         //change to cool
         this.mode=false
         this.angle=1
       }else{
         //change to
         this.mode=true
         this.angle=99
       }
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