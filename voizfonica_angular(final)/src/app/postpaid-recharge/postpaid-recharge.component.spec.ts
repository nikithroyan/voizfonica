import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PostpaidRechargeComponent } from './postpaid-recharge.component';

describe('PostpaidRechargeComponent', () => {
  let component: PostpaidRechargeComponent;
  let fixture: ComponentFixture<PostpaidRechargeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PostpaidRechargeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PostpaidRechargeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
