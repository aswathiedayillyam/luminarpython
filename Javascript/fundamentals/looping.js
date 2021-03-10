//let i=0;
// while(i<10){
 //   console.log(i);

// }



//ten to one

// let i=0;
// while(i>0){
//     console.log(i);
//     i--;
// }


// 1 is odd
// 2 is even up to 50

// let i=0;
// while(i<=50){
//     if(i%2==0){
//         // console.log("number"+i+"is odd");
//         console.log(`number ${i} is odd`);
//     }
//     else{
//         console.log(`number ${i} is even`)
//     }
//       i++;
// }


//for loop
//for(let i=0;i<=10;i++){
  //  console.log(i);
//}



// prime number checking
var number=17;

var flag=0;
//2,16
for(let i=2;i<number;i++){
    if(number%i==0){
        flag+=1;
        break
    }
    else{
        flag=0;
    }
}
if(flag==0){
    console.log("prime");
}
else{
    console.log("not prime");

}