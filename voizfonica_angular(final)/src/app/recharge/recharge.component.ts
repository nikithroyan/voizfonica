import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-recharge',
  templateUrl: './recharge.component.html',
  providers:[ApiService],
  styleUrls: ['./recharge.component.css']
})
export class RechargeComponent implements OnInit {

  constructor( private _api: ApiService) { }

  ngOnInit(): void {
  }

  result:any
  paymentdata(data:any)

  {
    this._api.paymentdata(data).subscribe((result)=>{console.warn(result)});
    alert("YOUR RECCHARGE IS DONE");
    data.reset()
   }

}
