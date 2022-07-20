import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-query',
  templateUrl: './query.component.html',
  providers:[ApiService],
  styleUrls: ['./query.component.css']
})
export class QueryComponent implements OnInit {

  constructor(private _api: ApiService) { }

  ngOnInit(): void {
  }

  result:any
  querydata(data:any, form1:NgForm)

  {
    this._api.querydata(data).subscribe((result)=>{console.warn(result)});
    alert("Your query is registered.We will contact you soon.");
    form1.reset()
  }

}
