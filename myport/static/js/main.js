document.addEventListener('DOMContentLoaded', function(){
    var portBtn = document.getElementById('open-port-form')
    var closePortModal = document.querySelector('.close-port-modal');


    var portModal = document.querySelector("[data-port-modal]")
    portBtn.addEventListener('click', ()=> {
        portModal.showModal()
        
    })

    closePortModal.addEventListener('click', ()=>{
        portModal.close()
    })


fdfd

// END OF DOMCONTENTLOADER
})

var activeItems = null;

function portList(){
    var wrapper = document.querySelector('.port-list');
    wrapper.innerHTML = "";

    var url = 'http://172.105.190.111:8000/portapi/port/port-list/'

    fetch(url)
    .then(response => response.json())
    .then((data) => {
        var list = data;
       
        for (i in list ){
            var item = `
            <div class="d-flex" id="data-row-${i}" >
            <div class="p-2 flex-fill flex-grow-1 title">${list[i].title} </div>
            
            <div> 
            <button class="p-2 flex-fill btn-info mb-1 edit"><i class="fa-regular fa-pen-to-square"></i></button>
            <button class="p-2 flex-fill btn-danger mb-1 delete"><i class="fa-solid fa-trash"></i></button>
            </div>
          </div><hr>
            `

            wrapper.innerHTML += item;
        }

        for (i in list){
            var editBtn = document.getElementsByClassName('edit')[i];
            var deleteBtn = document.getElementsByClassName('delete')[i];

             //  UPDATE BUTTONS HERE
        editBtn.addEventListener('click', (function(item){
            return function (){
                updatePort(item);
            }
        })(list[i]))

        // Delete button here 

        deleteBtn.addEventListener('click', (function(item){
            return function (){
                deleteItems(item);
            }
        })(list[i]))
        }

        
    })
    .catch((error) => console.log(error))
}

portList()

//====================================================================
//  CREATING POST FORM
// ==================================================================

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');



// To populate the category select field. 

fetch('http://172.105.190.111:8000/portapi/port/categories/')
.then((response) => response.json())
.then((categories)=>{
    const categorySelect = document.querySelector('#id_category'); // Update with your actual field ID
        categories.forEach(category => {
            const option = document.createElement('option');
            option.value = category.id;
            option.textContent = category.name;
            categorySelect.appendChild(option);
        });
    })
    .catch(error => {
        console.error('Error fetching categories:', error);

})

// Function to generate Slug
function generateSlug(title) {
    return title.toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]+/g, '');
}

// Get the form element
const titlesInput = document.getElementById('titles');
const slugsInput = document.getElementById('slugs');

// Add event listener to auto-generate slug based on title 
titlesInput.addEventListener('input', () => {
    const titleValue = titlesInput.value.trim();
    const generatedSlug = generateSlug(titleValue);
    slugsInput.value = generatedSlug;
});


// ===================================================

// start building the form inside the modal 
var portForm = document.getElementById('portForm');
 

portForm.addEventListener('submit', function(e) {
    e.preventDefault();
    var formData = new FormData(portForm);

    var url = 'http://172.105.190.111:8000/portapi/port/port-create/';
    if (activeItems != null) {
        var url = `http://172.105.190.111:8000/portapi/port/port-update/${activeItems.id}/`
        activeItems = null
    }

    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: formData,
    })
    .then((response) => response.text())
    .then(function(html){
        var portModal = document.querySelector("[data-port-modal]")
            portModal.close()

          return portList()
    })
    .catch(function(error) {
        console.log('Error', error);
    });
});


function updatePort(item){
    activeItems = item;
    console.log(activeItems)
    const portModal = document.querySelector("[data-port-modal]");
    portModal.showModal();

         // Assuming activeItem properties correspond to form field IDs
         document.getElementById('id_category').value = activeItems.category || '';
         document.getElementById('titles').value = activeItems.title || '';
         document.getElementById('slugs').value = activeItems.slug || '';
         document.getElementById('descriptions').value = activeItems.description || '';
         document.getElementById('embed_codes').value = activeItems.embed_code || '';
         document.getElementById('images').value = activeItems.image || '';
         document.getElementById('image_url').value = activeItems.image_url || '';
         document.getElementById('git_source_code').value = activeItems.git_source_code || '';
         
         
         // Set other form fields accordingly
    
}

function deleteItems(item){
    var url = `http://172.105.190.111:8000/portapi/port/port-delete/${item.id}`;
    var options = {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json', 
            'X-CSRFToken': csrftoken,
        }
    }

   fetch(url, options)
   .then((response)=>{
    portList()
   })

}