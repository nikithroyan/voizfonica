import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-invoice',
  templateUrl: './invoice.component.html',
  providers : [ApiService],
  styleUrls: ['./invoice.component.css']
})
export class InvoiceComponent implements OnInit {


  items:any;
  error:any;
  items2:any;
  constructor(private api: ApiService) { }

  ngOnInit(): void {
  this.get();
  this.get1();

  }

  get=()=> {
    this.api.bill().subscribe(
    data=>{ this.items=data;},
     );
         (error: any) => this.error = error
  }

  get1=()=> {
    this.api.bill1().subscribe(
    data=>{ this.items2=data;},
     );
         (error: any) => this.error = error
  }

}
