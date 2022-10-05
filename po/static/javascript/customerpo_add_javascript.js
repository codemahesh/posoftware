
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


let customer_name = document.getElementById("id_customer_name");
let customer_code = document.getElementById("id_customer_code");
let category = document.getElementById("id_category");
let place = document.getElementById('id_place');
let address = document.getElementById('id_address');

customer_code.addEventListener('change', getCustomerCode)

function getCustomerCode(e){
    let customer_code = e.target.value;
    const data = {id: customer_code};
    let url = "{% url 'customercode' %}";

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data),
    }).then((response)=>response.json())
    .then((data) => {
        console.log('Success:', data);
        customer_name.innerHTML = '<option value="" selected="">------</option>'
        for(let i =0; i<data.length; i++)
        { 
            customer_name.innerHTML += `<option value=${data[i]["customer_name"]} selected ="">${data[i]["customer_name"]}</option>`
        }
    })
    .catch((error) => {
        console.error('Error:', error);
      });
}