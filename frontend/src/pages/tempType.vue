<template>
  <div class="q-pa-md">
    <div class="q-col-gutter-md row items-start">
      <div class="col-6">
        <q-img
          src="statics\digital.jpg"
          style="width: 100%"
        >
          <div class="absolute-bottom text-subtitle1 text-center">
            digital
          </div>
                <q-btn to="/setTemp" label="select" color="primary" @click.stop="digital()"></q-btn>

        </q-img>
      </div>
      <div class="col-6">
        <q-img src="statics\knob.png">
          <div class="absolute-bottom text-center">
            knob
          </div>
                <q-btn to="/setKnob" label="select" color="primary" @click="knob()"></q-btn>    
        </q-img>
      </div> 
    </div>
  </div>
</template>

<script>

export default {
  methods:{
    digital () {
      this.$axios.post('http://127.0.0.1:5000/start',{type:'0'})
      .then(function (response) {
        console.log(success)
      })
      .catch(function (error) {
        console.log(error.response);
      
      });
          
    },

    knob () {
      this.$axios.post('http://127.0.0.1:5000/start',{type:'1'})
      .then(function (response) {
            console.log(success)
      })
      .catch(function (error) {
        console.log(error.response);
      });
          
    }
  }
}
</script>
