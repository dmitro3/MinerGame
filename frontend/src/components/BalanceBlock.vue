<template>
  <div class="bal">
    <p v-if="language == 'ru'" class="title">ВАШ БАЛАНС:</p>
    <p v-else class="title">BALANCE:</p>
    <div class="balance-block">
      <div class="balance">
        <div class="logo-background">
          <img class="logoSmall" src="../assets/logo-small.png" alt="">
        </div>
        <h1 class="balNum">{{ formatNumber(Math.floor(balance)) }}</h1>
      </div>
    </div>
    <div style="display: flex; align-items: center; margin-top: 10px; gap: 10px;" >
      <p class="subtitle" v-if="language == 'ru'">ПРИБЫЛЬ В ЧАС:</p>
      <p class="subtitle" v-else>PROFIT PER HOUR:</p>
      <div class="earning">
        {{ formatNumber(gph) }} YL
      </div>
      <div class="earning" id="multiplier">
        x{{ modifier }}
      </div>
    </div>
    
  </div>
</template>

<script>
export default {
  methods:{
    formatNumber(number) {
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    }
  },

  computed:{
    balance() {
      return this.$user.data.balance;
    },
    gph() {
      return this.$user.data.gph;
    },
    modifier(){
      return this.$user.data.modifier;
    },
    language(){
      return this.$user.data.lang;
    },
  }
}
</script>

<style scoped>
.bal{
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-direction: column;
  margin-bottom: 10px;
}
#multiplier{
  background: linear-gradient(0deg, rgb(233, 80, 80) 0%, rgb(220, 40, 40) 100%);
  margin-left: -5px;
}
.earning{

  width: fit-content;
  padding: 3px 10px;
  background: linear-gradient(180deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
  color: white;
  font-family: "Druk Wide";
  font-size: 8px;
  border-radius: 10px;
  filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
}

.subtitle{
  color: white;
  font-family: "Druk Wide";
  font-size: 6px;
  margin: 0;
}
.balance{
  width: 100%;
  display: flex;
  align-items: center;
}
.logo-background{
  width: 50px;
  height: 50px;
  background: linear-gradient(180deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.logoSmall{
  width: 35px;
  height: 25px;
}
.title{
  
  color: white;
  font-family: "Druk Wide";
  font-size: 8px;
  margin: 0;
  margin-top: 10px;
}
.balance-block{
  width: 80vw;
  padding: 5px;
  height: 50px;
  background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
  border-radius: 35px;
  filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
}
.balNum{
  text-align: center;
  margin: 0;
  margin-top: 10px;
  margin-bottom: 5px;
  color: white;
  font-family: "Druk Wide";
  font-size: 22px;
  width: 80%;
}
</style>