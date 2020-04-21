<template>
  <q-page class="flex flex-center ">


        <q-btn v-if="mode" label="change mode" color="red" @click="changeMode()"  ></q-btn> 
          <q-btn v-else label="change mode" color="blue" @click="changeMode()" ></q-btn> 
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
      
      <q-btn label="submit" color="primary" @click="setTemp()"></q-btn> 
          
  </q-page>
</template>

<script>
export default {
  data(){
    return  {
      newtext : '',
      set : 0,
      angle:100,
      mode : true,
    }
  },
  methods:{
    setTemp(){
      var navigate = this.$router;
      var res
      
      if(this.mode){
        res=100-this.angle
      }else{
        res=this.angle
      }
      console.log(res)
     this.$axios.post('http://127.0.0.1:5000/setKnob',{temp:res})
      .then(function (response) {
        
        navigate.push("./knob")

      })
      .catch(function (error) {
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