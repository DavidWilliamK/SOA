import axios from 'axios'

export default {
    name: "Home",
    data () {
        return {
            alertText: '',
            files: [],
            detected: []
        }
    },
    created () {
        axios({
            method: 'get',
            url: `https://www.foaas.com/dosomething/upload/image/anon`,
        }).then((response) => {
            this.alertText = response.data.message.charAt(0).toUpperCase() + response.data.message.slice(1)
        }, (error) => {
            console.log(error)
        })
    },
    computed: {

    },
    methods: {
        detect() {
            let formData = new FormData()
            let configuration = { headers: { 'Content-Type': 'multipart/form-data' } }
            this.files.forEach((file, idx) => {
                formData.append('files['+idx+']', file)
                formData.append('name['+idx+']', JSON.stringify(file.name))
            })
            formData.append('count', JSON.stringify(this.files.length))
            this.predict(formData, configuration)
        },
        predict(formData, configuration) {
            axios({
                method: 'post',
                url: `http://127.0.0.1:5000/save`,
                configuration,
                data: formData
            }).then((res) => {
                this.detected = res
                console.log('YAY')
            }, (error) => {
                console.log(error)
            })
        }
    }
}