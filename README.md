
Article on databases: https://www.researchgate.net/publication/327808220_The_DriveU_Traffic_Light_Dataset_Introduction_and_Comparison_with_Existing_Datasets <br> <br>

## Results
Faster R-CNN FPN on Lisa dataset, 3 epochs, batch = 16, LR_on_plateau, Adam <br>
https://drive.google.com/file/d/1h7PfPPYH8ZyR1egjDF1vl0-83aseZHR-/view?usp=sharing <br>
Performance on test video: https://drive.google.com/file/d/1F-1yy4BSjNHT75andGyOidVUf_m__CGx/view?usp=sharing <br> <br>
Faster R-CNN on Lisa+Bosch datasets, 8k+8k photos, 3 epochs <br>
https://drive.google.com/file/d/1RiIs1-aqPIEr4a_EP64SnuQvvmZNubeP/view?usp=sharing <br>
Perfomance on test video: https://drive.google.com/file/d/12P5xmOzrwSSlhCHv7AHcfIB0U6CP6A11/view?usp=sharing <br><br>
8 epochs with Bosch, Lisa and S2TLD datasets <br>
https://drive.google.com/file/d/1zrfmFG5lz84of6Ul7e0USBSlIyzdm2ZX/view?usp=sharing <br> <br>
Detection at night <br>
https://drive.google.com/file/d/16lRq48L-5rzCxDWzMRgPQ5FR5rmwFm-4/view?usp=sharing


## Some info

I used Faster RCNN to find traffic lights on video. Training data consists of LISA, Bosch and S2TLD datasets. You can find links for this datasets in "useful links" file. The code with downloading all datasets is in Datasets.ipynb file. <br><br>
You can find some expirements with night data in "Detection/" directory (Night model training.ipynb). <br><br>
Faster RCNN gives good results in finding traffic lights but one main downside is speed. So, since Faster RCNN is not fast enough to find boxes for each frame, each 4-th frame was processed. <br><br> 

## Experiments

The experiments included attempts to use the Yolo model and the transformer DETR. It was especially interesting to test the second approach because the transformer architecture for images is a new idea, and a paper with it was published on May 28th, 2020 (https://arxiv.org/abs/2005.12872). It was manageable to detect traffic lights, i.e. one class using this network (DETR experiment.ipynb). With YOLO there were difficulties primarily with the interaction with google colab. Many settings for successful operation of this network are Linux-friendly, which was not available. <br>
Thus, the Faster R-CNN architecture with the FPN backbone was used in this paper. You can read more about its work in the following article: https://jonathan-hui.medium.com/understanding-feature-pyramid-networks-for-object-detection-fpn-45b227b9106c. For convenience a brief and informal description of all neural networks was created, this file was meant only to facilitate understanding of the architectures: Architectures.pdf. <br><br>


Every file with .py extension is in pep8 format and contains the main component from final .ipynb file. <br><br>
resize.py <br>
configuration.py <br>
transforms.py <br>
dataloaders.py <br>
model_training.py <br>
inference.py <br> <br>


You can find final .ipynb file in "/Detection" folder (The final code of training the model.ipynb.) . ALso this folder contains some of experiments.<br>



/**
* Name: NewModel
* Based on the internal empty template. 
* Author: perrymad
* Tags: 
*/


model NewModel

global {
/** Insert the global definitions,
* variables and actions here
*/
float max_carrying_capacity <- 10.0;
float growth_rate <- 0.2 ;
float max_cabbages_eat <- 2.0;
float reproduction_threshold <- 20.0;
float initial_energy <- 10.0;
init {
	create goat number: 100;
	create wolf number: 5;
	}

}


/* Insert your model definition here */
grid plot height: 30 width: 30 neighbors: 8 {
	bool is_free;
	float biomass;
	float biomass_ratio;
	float carrying_capacity;
	rgb color <- rgb(255*(1-biomass/max_carrying_capacity),255, 255*(1-biomass/max_carrying_capacity))
		update: rgb(255*(1-biomass/max_carrying_capacity),255,255*(1-biomass/max_carrying_capacity));
	

	init {
		carrying_capacity <- rnd(max_carrying_capacity);
		biomass_ratio <- rnd(carrying_capacity)/max_carrying_capacity;
		color <- rgb(255*(1-biomass_ratio),255,255*(1-biomass_ratio));
		}
		
	aspect plotCarryingCapacity {
		draw square(1) color: rgb(0,255*carrying_capacity/max_carrying_capacity,0);
	}

	reflex grow {
		if(carrying_capacity != 0){
			biomass <- biomass*(1 + growth_rate * (1 - biomass/carrying_capacity));
		}
	}
}

//species wolf {
//	plot my_plot;
//	
//	init {
//		location <- one_of(plot).location;
//		my_plot <- one_of(plot where (each.is_free = true));
//		location <- my_plot.location;
//		my_plot.is_free <- false;
//		
//		plot random_plot <- one_of(plot where (each.is_free = true));
//		do move_to_cell(random_plot);
//	}
//	
//	reflex move {
//		plot next_plot <- one_of(my_plot.neighbors
//		where(each.is_free = true));
//		my_plot.is_free <- true;
//		next_plot.is_free <- false;
//		my_plot <- next_plot;
//		location <- next_plot.location;
//		
//		do move_to_cell(next_plot);
//		}	
//		
//	action move_to_cell(plot new_plot) {
//		if(my_plot != nil) {
//		my_plot.is_free <- true;
//		}
//		new_plot.is_free <- false;
//		my_plot <- new_plot;
//		location <- new_plot.location;
//	}
//	aspect redCircle {draw circle(1) color: #red;}
//}
//	
//species goat {
//	plot my_plot;
//	init {
//		location <- one_of(plot).location;
//		my_plot <- one_of(plot where (each.is_free = true));
//		location <- my_plot.location;
//		my_plot.is_free <- false;
//		
//		plot random_plot <- one_of(plot where (each.is_free = true));
//		do move_to_cell(random_plot);
//	}
//	reflex move {
//		plot next_plot <- one_of(my_plot.neighbors
//		where(each.is_free = true));
//		my_plot.is_free <- true;
//		next_plot.is_free <- false;
//		my_plot <- next_plot;
//		location <- next_plot.location;
//		
//		do move_to_cell(next_plot);
//		}	
//		

//	}	
//	
//	aspect blueSquare {draw square(1) color: #blue;}
//}



species animal {
	plot my_plot;
	float energy <- initial_energy;
	
	init {
		location <- one_of(plot).location;
		my_plot <- one_of(plot where (each.is_free = true));
		location <- my_plot.location;
		my_plot.is_free <- true;
	}	
	
	reflex move {
		plot next_plot <- one_of(my_plot.neighbors where(each.is_free = true));
		my_plot.is_free <- true;
		next_plot.is_free <- false;
		my_plot <- next_plot;
		location <- next_plot.location;
	}	
	// Other reflexes
	reflex energy_loss {
		energy <- energy - 1;
	}
	reflex death when: energy <= 0.0 {
		do die;
	}	
	// Reproduce
	reflex reproduce when: energy >= reproduction_threshold {
		plot plot_for_child <- one_of(my_plot.neighbors
		where(each.is_free = true));
		if(plot_for_child != nil) {
			create species(self) number: 1 {
			do move_to_cell(plot_for_child);
			self.energy <- myself.energy / 2;}
			energy <- energy / 2;}
	}		
	
	action move_to_cell(plot new_plot) {
		if(my_plot != nil) {my_plot.is_free <- true;}
		new_plot.is_free <- false;
		my_plot <- new_plot;
		location <- new_plot.location;
	}	
}
	
		
species wolf parent: animal {
	aspect redCircle {
		draw circle(1) color: #red;
	}
	
	reflex move {
		plot next_plot <- nil;
		list<plot> neigh <-
		my_plot.neighbors where(!empty(goat inside each));
		if(empty(neigh)) {
			next_plot <- one_of(my_plot.neighbors
				where(each.is_free = true));
		} 
		else {
			next_plot <- one_of(neigh);
			goat victim <- one_of(goat inside next_plot);
			energy <- energy + victim.energy;
			ask victim {
				write "" + self + " will die";
				do die;
			}
		}
		do move_to_cell(next_plot);
	}
}

species goat parent: animal {
	reflex eat_cabbage {
		float cab <- min([max_cabbages_eat, my_plot.biomass]);
		energy <- energy + cab;
		my_plot.biomass <- my_plot.biomass - cab;
	}
	aspect blueSquare {
		draw square(2) color: #blue;
	}
}


experiment cabbagesExp type: gui {
	output {
		display biomass {
			grid plot lines: #black;
			species wolf aspect: redCircle;
			species goat aspect: blueSquare;
		}
		display plots {
		chart "Nb animals" type: series {
			data "#wolves" value: length(wolf);
			data "#goats" value: length(goat);
			}
		}
	}
}


