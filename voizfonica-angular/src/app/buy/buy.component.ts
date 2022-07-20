import { Component, OnInit } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../api.service';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-buy',
  templateUrl: './buy.component.html',
  providers:[ApiService],
  styleUrls: ['./buy.component.css']
})
export class BuyComponent implements OnInit {

  constructor(private _api: ApiService) { }

  ngOnInit(): void {
  }


  result:any
  customerdata(data:any,form1:NgForm)

  {
    this._api.customerdata(data).subscribe((result)=>{console.warn(result)});
    alert("THANK YOU FOR JOINING VOIZFONICA");
    form1.reset()
   }

}

