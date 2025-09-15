let n = 0;
        const num = document.getElementById("num");

        document.getElementById("add").addEventListener("click", function () {
            n++;
            num.innerHTML = n;
        });
        document.getElementById("push").addEventListener("click", function () {
            location.href = 'http://10.150.3.199:5000/save/' + n;
            n = 0;
            num.innerHTML = n;
        });
