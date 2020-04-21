<template>
   
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
      
</template>

<script>
export default {
  data(){
    return{
      angle:100,
      mode : false
    }
  },
  methods:{
     check(newangle){
      //  if(this.mode){
      //   if(newangle<50){
      //      this.angle=50
      //   }
      //  }else{
       
      //    if (newangle>50&&newangle<100){
      //     this.angle=50
      //   }
      //  }
       console.log(this.angle)
     },
     changeMode(){
       if(this.mode){
         //change to cool
         this.mode=false
         angle=100
       }else{
         //change to
         this.mode=true
         angle=0
       }
     }
     
  }



}
</script>
