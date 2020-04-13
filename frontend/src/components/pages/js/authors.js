import axios from 'axios'

export default {
    name: "Authors",
    data() {
        return {
            imageSrc: ''
        }
    },
    created () {
        this.findDog()
    },
    methods: {
       findDog() {
           axios({
               method: 'get',
               url: `https://random.dog/woof.json`,
           }).then((response) => {
               this.imageSrc = response.data.url
           }, (error) => {
               console.log(error)
           })
       }
    }
}