let viTriKeyword = [
'English teaching assistant',
'Chuyên viên sap basis',
'Human resource assistant',
'Warehouse assistant',
'Customer services assistant',
];
let nganhNgheKeyword = [
    'Hàng hải',
    'Hàng không',
    'IT phần mềm',
    'IT phần cứng / Mạng',
    'Khách sạn / Nhà Hàng',
];
let kyNangKeyword = [
    '.Net',
    '3D Artist',
    '3D Max',
    'HTML',
    'C#',
    'C++',
];
let addressKeyword = [
    'TP.Hồ Chí Minh',
    'Đà Nẵng',
    'Hà Nội',
    'Bến Tre',
    'Bình Định',
    'Vũng Tàu',
];
const resultsBox = document.querySelector("#result-box");
const inputViTriBox = document.getElementById("inputBox");
const tagBox = document.querySelector('#tag')

const resultsBox1 = document.querySelector("#result-box1");
const inputNganhNgheBox = document.getElementById("inputBox1");
const tagBox1 = document.querySelector('#tag1')

const resultsBox2 = document.querySelector("#result-box2");
const inputKyNangBox = document.getElementById("inputBox2");
const tagBox2 = document.querySelector('#tag2')

const resultsBox3 = document.querySelector("#result-box3");
const inputAddressBox = document.getElementById("inputBox3");
const tagBox3 = document.querySelector('#tag3')
// --------------------- ViTri
inputBox.onkeyup = function(){
    let result = [];
    let input = inputViTriBox.value;
    if (input.length){
        result = viTriKeyword.filter((keyword) => {
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
    }
    display(result);
    if(!result.length){
        resultsBox.innerHTML='';
    }
}

function display(result){
    const content = result.map((list)=>{
        return "<li onclick=selectInput(this)>" + list + "</li>";
    });
    resultsBox.innerHTML = "<ul>" + content.join('') + "</ul>";
}

function selectInput(list){
    tagBox.innerHTML += '<li onclick=deleteTag(this)><i class="fa fa-times" aria-hidden="true"></i>'+' '+ list.innerHTML +'</li>';
    inputViTriBox.value='';
    resultsBox.innerHTML='';
}

// --------------------- Nganh Nghe
inputBox1.onkeyup = function(){
    let result = [];
    let input = inputNganhNgheBox.value;
    if (input.length){
        result = nganhNgheKeyword.filter((keyword) => {
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
    }
    displayNganhNghe(result);
    if(!result.length){
        resultsBox1.innerHTML='';
    }
}

function displayNganhNghe(result){
    const content = result.map((list)=>{
        return "<li onclick=selectInputNganhNghe(this)>" + list + "</li>";
    });
    resultsBox1.innerHTML = "<ul>" + content.join('') + "</ul>"
}

function selectInputNganhNghe(list){
    tagBox1.innerHTML += '<li onclick=deleteTag(this)><i class="fa fa-times" aria-hidden="true"></i>'+' '+ list.innerHTML +'</li>';
    inputNganhNgheBox.value='';
    resultsBox1.innerHTML='';
}
// --------------------- KyNang
inputBox2.onkeyup = function(){
    let result = [];
    let input = inputKyNangBox.value;
    if (input.length){
        result = kyNangKeyword.filter((keyword) => {
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
    }
    displayKyNang(result);
    if(!result.length){
        resultsBox2.innerHTML='';
    }
}

function displayKyNang(result){
    const content = result.map((list)=>{
        return "<li onclick=selectInputKyNang(this)>" + list + "</li>";
    });
    resultsBox2.innerHTML = "<ul>" + content.join('') + "</ul>"
}

function selectInputKyNang(list){
    tagBox2.innerHTML += '<li onclick=deleteTag(this)><i class="fa fa-times" aria-hidden="true"></i>'+' '+ list.innerHTML +'</li>'
    inputKyNangBox.value='';
    resultsBox2.innerHTML='';
}
// --------------------- DiaChi
inputBox3.onkeyup = function(){
    let result = [];
    let input = inputAddressBox.value;
    if (input.length){
        result = addressKeyword.filter((keyword) => {
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
    }
    displayAddress(result);
    if(!result.length){
        resultsBox3.innerHTML='';
    }
}

function displayAddress(result){
    const content = result.map((list)=>{
        return "<li onclick=selectInputAddress(this)>" + list + "</li>";
    });
    resultsBox3.innerHTML = "<ul>" + content.join('') + "</ul>"
}

function selectInputAddress(list){
    tagBox3.innerHTML += '<li onclick=deleteTag(this)><i class="fa fa-times" aria-hidden="true"></i>'+' '+ list.innerHTML +'</li>'
    inputAddressBox.value='';
    resultsBox3.innerHTML='';
}
// --- Xóa
function deleteTag(tag){
    tag.remove();
}
