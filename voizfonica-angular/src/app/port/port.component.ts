import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-port',
  templateUrl: './port.component.html',
  providers:[ApiService],
  styleUrls: ['./port.component.css']
})
export class PortComponent implements OnInit {

  constructor(private _api: ApiService) { }

  ngOnInit(): void {
  }


  result:any
  getvalues(data:any,form1:NgForm)

  {
    this._api.getvalues(data).subscribe((result)=>{console.warn(result)});
    alert("THANK YOU FOR JOINING VOIZFONICA");
    form1.reset()
   }

}
