import { Component } from '@angular/core';
import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AboutUsComponent } from './pages/about-us/about-us.component';
import { SegmentationSpaceComponent } from './pages/segmentation-space/segmentation-space.component';

export const routes: Routes = [
    {
        path: '',
        redirectTo: 'Home',
        pathMatch: 'full'
    },
    {
        path:'Home',
        component :HomeComponent
    },
    {
        path:'About-Us',
        component:AboutUsComponent
    },
    {
        path: 'Segmentation-Space',
        component:SegmentationSpaceComponent
    }


];
