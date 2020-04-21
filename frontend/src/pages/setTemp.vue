<template>
  <q-page class="flex flex-center">
      <q-input @keyup.enter="setTemp()" v-model="newtext" placeholder="Current Temp setting" stack-label dense for='tempSet'/>
      <q-btn  label="submit" color="primary" @click="setTemp()"></q-btn> 
  </q-page>
</template>

<script>
export default {
  data(){
    return  {
      newtext : ''
    }
  },
  methods:{
    setTemp(){
      var navigate = this.$router;
     this.$axios.post('http://127.0.0.1:5000/setTemp',{temp:this.newtext})
      .then(function (response) {
        
          navigate.push("./digital")
        
      })
      .catch(function (error) {
        console.log(error.response);
      
      });
    }
  }
}
</script>