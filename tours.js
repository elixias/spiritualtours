const request = require("superagent");
var cheerio = require("cheerio");
var fs = require("fs");


async function saveDetails(){
var result = await request.get('https://www.bookmeditationretreats.com/koom-retreat-and-training-center/4-days-of-internal-chinese-martial-arts-and-sufi-initiation-in-marrakech-morocco');
var res = cheerio.load(result.text);
await fs.writeFile("result.txt",result.text,function(err){console.log("Saved.");});
}
//saveDetails();return;	

async function start(){
fs.readFile('data2.txt','utf-8',(err,data)=>{
	extractDetails(data);
})
}
//start(); return;

async function extractDetails(pageURL){
	try{
	var data = await request.get(pageURL);
	data = data.text;

	var res = cheerio.load(data);
	var title = res('.listing-title .title').text().replace(/[^\w\s]/gi, '')
	var loc = res('.listing-title__location').text().replace(/[^\w\s]/gi, '')
	var specloc = loc.split(" ").pop()
	var pattern = new RegExp('The maximum participants in the group is [0-9]+')
	var parts = pattern.exec(res('div.listing-overview__notes').text())
	var people = (parts==null)?"":parts.toString().split(" ").pop();
	var dur = new RegExp('[0-9]+ days').exec(res('div.listing-overview__notes').text()).toString().split(' ').shift()
	var listing = res('.listing-packages .input-wpr').children();
	var accom = '';
	listing.each((i,elem)=>{
		//console.log(res('p',elem).text());
	})
	
	var ind = data.indexOf('dataLayer.push({"packages":')
	var ind2 = data.indexOf('});',ind)
	
	var pricing = JSON.parse(data.substr(ind+15,ind2-ind-14))
	var lowest = pricing.packages[0].packagePrice;
	var priceAll = pricing.packages.map((pkg)=>{return `${pkg.packagePersons} Persons,${pkg.packageRoomType},${pkg.packageAccomodationType},${pkg.packagePrice}`}).join('\n');
	
	console.log(title);
	console.log(loc);
	console.log(people);
	console.log(dur);
	console.log(lowest);
	console.log(priceAll);
	return `"${title}","${loc}","${specloc}","${people}","${dur}","${lowest}","${priceAll}"\r\n`;
	}catch (e){
		return 'ERR,ERR,ERR,ERR,ERR,ERR,ERR';
	}
}

let main = async () => {

	var allData = "";
	console.log("Starting...");
	//page 1 to 10 done
	//max is 194
	for(var page = 11;page<=194;page++){
		console.log("Scanning page "+page);
		//var url = 'https://www.google.com'
		var url = 'https://www.bookmeditationretreats.com';
		var result = await request.get(url+'?page='+page);
		var res = cheerio.load(result.text);
		console.log("Processing...")
		var data = res('#start-discovering div.t-row .showcards-wrapper .cards').children();
		
		for(d in data){//12
			if (d<12){
				allData+=await extractDetails(url+res('.showcards a', data[d]).attr('href'));
			}
		}
	}
	
	fs.writeFile("result.txt",allData,function(err){console.log("Saved.");});
	
}

main();


//write to file:

